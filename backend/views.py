import os
import json
import sqlparse
from collections import OrderedDict

from .models import *
from .serializers import *

from django.db import connection
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class Campuses(APIView):
    """
    API endpoint that outputs the name of all the campuses.
    """
    def get(self, request, format=None):
        campuses = MapsInstitutions.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)

class Degrees(APIView):
    """
    API endpoint that outputs the name of all the degrees for a particular campus.
    """
    def get(self, request, id, format=None):
        degrees = MapsAcadPlan.objects.filter(institute_id=id)
        serializer = DegreesSerializer(degrees, many=True)

        if degrees.exists():
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class Course(viewsets.ViewSet):
    """
    API endpoint for courses in course catalog
    """
    """
    Get a course's details by course ID
    """
    def retrieve(self, request, crse_id=None): #get a course by id

        serializer_context = {
            'request': request,
        }
        course = MapsCrseCatalog.objects.filter(course_id=crse_id)
        serializer = CourseSerializer(course, context=serializer_context, many=True)

        if course.exists():
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    """ 
    Search a course by institution, and name, or description
    """
    @action(detail=True, methods=['get'])
    def search(self, request, *args, **kwargs):
        q = request.query_params.get('q')
        id = request.query_params.get('id')
        major = request.query_params.get('major')

        if q is None or id is None or major is None:
            return Response({'message' : 'invalid query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        queries = get_queries_from_file('findCourse.sql')

        with connection.cursor() as cursor:
            cursor.execute(queries[0], [id])
            cursor.execute(queries[1], [major])
            cursor.execute(queries[2], [q])
            cursor.execute(queries[3])
            rows = cursor.fetchall()

        # Parse results to json format
        result = []
        keys = ('course_id', 'eff_date', 'institute_id', 'status', 'subject', 'catalog', 'descr', 'min_units', 'max_units')

        for row in rows:
            result.append(OrderedDict(zip(keys,row)))

        if(len(result) == 0):
            return Response({ 'message': 'No matching courses found' }, status=status.HTTP_200_OK)
        
        else:
            json_data = json.dumps(result, indent=4, default=str)
            return HttpResponse(json_data, content_type="application/json")


class Map(viewsets.ViewSet):
    """
    Get a map by map_id
    TODO:Return all maps for a particular institution and major
    """
    @action(detail=True, methods=['get'])
    def get_map_by_id(self, request, map_id, format=None):
        # Get and execute query from file
        queries = get_queries_from_file("returnMapsInfo.sql")

        if not mapExists(map_id):
            return Response({ 'message' : 'map_id does not exist'}, status=status.HTTP_404_NOT_FOUND)

        with connection.cursor() as cursor:
            cursor.execute(queries[0], [map_id])
            cursor.execute(queries[1])
            rows = cursor.fetchall()

        # Parse results to json format
        result = []
        keys = ('map_id','semester_num','course_id', 'subject', 'catalog', 'descr', 'min_units', 'max_units', 'designation')

        for row in rows:
            result.append(OrderedDict(zip(keys,row)))

        json_data = json.dumps(result, indent=4)

        return HttpResponse(json_data, content_type="application/json")
    
    """
    Delete a map by map_id
    """
    @action(detail=True, methods=['delete'])
    def delete_map_by_id(self, request, map_id, format=None):
        # TODO: Authorization

        queries = get_queries_from_file("deleteMaps.sql")

        if not mapExists(map_id):
            return Response({ 'message' : 'map_id does not exist'}, status=status.HTTP_404_NOT_FOUND)

        with connection.cursor() as cursor:
            cursor.execute(queries[0], [map_id])
            cursor.execute(queries[1])
            cursor.execute(queries[2])
           
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    """
    Edit existing map by map_id
    """
    @action(detail=True, methods=['put'])
    def edit_map_by_id(self, request, map_id, format=None):
        return Response({}, status=status.HTTP_200_OK, content_type="application/json")

    """
    Add a new map
    """
    @action(detail=True, methods=['post'])
    def create_map(self, request, format=None):
        queries = get_queries_from_file("insertMapBlank.sql")

        for q in range(0, len(queries)):
            print(str(q) + "   :  "  + queries[q])
        # is there an elegant solution?
        with connection.cursor() as cursor:
            # Gather Meta Info
            cursor.execute(queries[0], [request.data["map_name"]])
            cursor.execute(queries[1], [request.data["degree"]])
            cursor.execute(queries[2], [request.data["start_year"]])
            cursor.execute(queries[3])
            cursor.execute(queries[4], [request.data["institute_id"]])
            cursor.execute(queries[5], [request.data["submit_id"]])
            cursor.execute(queries[6])
            cursor.execute(queries[7])
            cursor.execute(queries[8])

            # Insert Meta info into MAPS_DMAPS_META
            cursor.execute(queries[9]) 

            # Prepare courses for insert
            cursor.execute(queries[10])
            cursor.execute(queries[11], [checkNullCourse(request.data["sem1_class1"])])
            cursor.execute(queries[12], [checkNullCourse(request.data["sem1_class2"])])
            cursor.execute(queries[13], [checkNullCourse(request.data["sem1_class3"])])
            cursor.execute(queries[14], [checkNullCourse(request.data["sem1_class4"])])
            cursor.execute(queries[15], [checkNullCourse(request.data["sem1_class5"])])
            cursor.execute(queries[16], [checkNullCourse(request.data["sem1_class6"])])
            cursor.execute(queries[17], [checkNullCourse(request.data["sem1_class7"])])
            cursor.execute(queries[18], [checkNullCourse(request.data["sem2_class1"])])
            cursor.execute(queries[19], [checkNullCourse(request.data["sem2_class2"])])
            cursor.execute(queries[20], [checkNullCourse(request.data["sem2_class3"])])
            cursor.execute(queries[21], [checkNullCourse(request.data["sem2_class4"])])
            cursor.execute(queries[22], [checkNullCourse(request.data["sem2_class5"])])
            cursor.execute(queries[23], [checkNullCourse(request.data["sem2_class6"])])
            cursor.execute(queries[24], [checkNullCourse(request.data["sem2_class7"])])
            cursor.execute(queries[25], [checkNullCourse(request.data["sem3_class1"])])
            cursor.execute(queries[26], [checkNullCourse(request.data["sem3_class2"])])
            cursor.execute(queries[27], [checkNullCourse(request.data["sem3_class3"])])
            cursor.execute(queries[28], [checkNullCourse(request.data["sem3_class4"])])
            cursor.execute(queries[29], [checkNullCourse(request.data["sem3_class5"])])
            cursor.execute(queries[30], [checkNullCourse(request.data["sem3_class6"])])
            cursor.execute(queries[31], [checkNullCourse(request.data["sem3_class7"])])
            cursor.execute(queries[32], [checkNullCourse(request.data["sem4_class1"])])
            cursor.execute(queries[33], [checkNullCourse(request.data["sem4_class2"])])
            cursor.execute(queries[34], [checkNullCourse(request.data["sem4_class3"])])
            cursor.execute(queries[35], [checkNullCourse(request.data["sem4_class4"])])
            cursor.execute(queries[36], [checkNullCourse(request.data["sem4_class5"])])
            cursor.execute(queries[37], [checkNullCourse(request.data["sem4_class6"])])
            cursor.execute(queries[38], [checkNullCourse(request.data["sem4_class7"])])
            cursor.execute(queries[39], [checkNullCourse(request.data["sem5_class1"])])
            cursor.execute(queries[40], [checkNullCourse(request.data["sem5_class2"])])
            cursor.execute(queries[41], [checkNullCourse(request.data["sem5_class3"])])
            cursor.execute(queries[42], [checkNullCourse(request.data["sem5_class4"])])
            cursor.execute(queries[43], [checkNullCourse(request.data["sem5_class5"])])
            cursor.execute(queries[44], [checkNullCourse(request.data["sem5_class6"])])
            cursor.execute(queries[45], [checkNullCourse(request.data["sem5_class7"])])
            cursor.execute(queries[46], [checkNullCourse(request.data["sem6_class1"])])
            cursor.execute(queries[47], [checkNullCourse(request.data["sem6_class2"])])
            cursor.execute(queries[48], [checkNullCourse(request.data["sem6_class3"])])
            cursor.execute(queries[49], [checkNullCourse(request.data["sem6_class4"])])
            cursor.execute(queries[50], [checkNullCourse(request.data["sem6_class5"])])
            cursor.execute(queries[51], [checkNullCourse(request.data["sem6_class6"])])
            cursor.execute(queries[52], [checkNullCourse(request.data["sem6_class7"])])
            cursor.execute(queries[53], [checkNullCourse(request.data["sem7_class1"])])
            cursor.execute(queries[54], [checkNullCourse(request.data["sem7_class2"])])
            cursor.execute(queries[55], [checkNullCourse(request.data["sem7_class3"])])
            cursor.execute(queries[56], [checkNullCourse(request.data["sem7_class4"])])
            cursor.execute(queries[57], [checkNullCourse(request.data["sem7_class5"])])
            cursor.execute(queries[58], [checkNullCourse(request.data["sem7_class6"])])
            cursor.execute(queries[59], [checkNullCourse(request.data["sem7_class7"])])
            cursor.execute(queries[60], [checkNullCourse(request.data["sem8_class1"])])
            cursor.execute(queries[61], [checkNullCourse(request.data["sem8_class2"])])
            cursor.execute(queries[62], [checkNullCourse(request.data["sem8_class3"])])
            cursor.execute(queries[63], [checkNullCourse(request.data["sem8_class4"])])
            cursor.execute(queries[64], [checkNullCourse(request.data["sem8_class5"])])
            cursor.execute(queries[65], [checkNullCourse(request.data["sem8_class6"])])
            cursor.execute(queries[66], [checkNullCourse(request.data["sem8_class7"])])

            # Insert courses into MAPS_DMAPS_LISTS
            cursor.execute(queries[67])

        return Response( { "message": "map successfully created." }, status=status.HTTP_201_CREATED, content_type="application/json")

def checkNullCourse(course_input):
    if course_input is "":
        return None
    return course_input

def mapExists(map_id):
    """
    Check if a map exists in the database
    """
    with connection.cursor() as c:
        c.execute("SELECT map_id FROM MAPS_DMAPS_LISTS WHERE map_id = %s", [map_id])
        rows = c.fetchall()
    
    for r in rows:
        print(r) 

    if len(rows) == 0:
        return False
    return True
    
def get_queries_from_file(filename):
    """ 
    Parses a sql file and returns sql queries as a list
    """
    with open(os.path.join('backend', 'queries', filename), 'r') as file:
        query_string = ""
        for line in file:
            if line.startswith("-"): #Skip comments    
                continue
            else:
                query_string += line.replace('\n', ' ')

    queries = sqlparse.split(query_string)
   
    return queries