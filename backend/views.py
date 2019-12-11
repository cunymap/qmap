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
            # json_data = json.dumps(result, indent=4, default=str)
            # return HttpResponse(json_data, content_type="application/json")
            return Response(result, status=status.HTTP_200_OK)


class Map(viewsets.ViewSet):

    @action(detail=True, methods=['get'])
    def map_by_institute_majorId(self, request, *args, **kwargs):
        
        institute_id = request.query_params.get('id')
        degree = request.query_params.get('major')
        start_year = request.query_params.get('start_year')

        # Validate inputs
        if institute_id is None or degree is None:
            return Response({ 'message': 'malformed query'}, status=status.HTTP_400_BAD_REQUEST)


        if start_year is not None:
        # Return the latest map by institution_id, major, and start_year

            queries = get_queries_from_file("findLatestMap.sql")

            with connection.cursor() as cursor:
                cursor.execute(queries[0], [institute_id])
                cursor.execute(queries[1], [degree])
                cursor.execute(queries[2], [start_year])
                cursor.execute(queries[3])
                cursor.execute(queries[4])
                result = cursor.fetchone()

            if result is None:
                return Response( { 'message': 'No maps were found' }, status=status.HTTP_404_NOT_FOUND )
            
            return Response( { "map_id" : result[0] }, status=status.HTTP_200_OK)

        else:
        # Return all maps available for an institution and major

            query = "select map_id, start_year from MAPS_DMAPS_META where institute_id=%s and degree=%s"

            with connection.cursor() as cursor:
                cursor.execute(query, [institute_id, degree])
                rows = cursor.fetchall()

            keys = ('map_id', 'start_year')
            result = []

            for row in rows:
                row = (row[0], row[1].replace('SP', 'Spring', 1))
                row = (row[0], row[1].replace('FA', 'Fall', 1))
                result.append(OrderedDict(zip(keys,row)))

            if len(result) == 0:
                return Response({"message": "no maps found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(result, status=status.HTTP_200_OK)


    """
    Get a map by map_id
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

        return Response(result, status=status.HTTP_200_OK)
    
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

        semX_classY = {
            "sem1_class1" : None, "sem1_class2" : None, "sem1_class3" : None, "sem1_class4" : None, "sem1_class5" : None, "sem1_class6" : None, "sem1_class7" : None,
            "sem2_class1" : None, "sem2_class2" : None, "sem2_class3" : None, "sem2_class4" : None, "sem2_class5" : None, "sem2_class6" : None, "sem2_class7" : None,
            "sem3_class1" : None, "sem3_class2" : None, "sem3_class3" : None, "sem3_class4" : None, "sem3_class5" : None, "sem3_class6" : None, "sem3_class7" : None,
            "sem4_class1" : None, "sem4_class2" : None, "sem4_class3" : None, "sem4_class4" : None, "sem4_class5" : None, "sem4_class6" : None, "sem4_class7" : None, 
            "sem5_class1" : None, "sem5_class2" : None, "sem5_class3" : None, "sem5_class4" : None, "sem5_class5" : None, "sem5_class6" : None, "sem5_class7" : None,
            "sem6_class1" : None, "sem6_class2" : None, "sem6_class3" : None, "sem6_class4" : None, "sem6_class5" : None, "sem6_class6" : None, "sem6_class7" : None,
            "sem7_class1" : None, "sem7_class2" : None, "sem7_class3" : None, "sem7_class4" : None, "sem7_class5" : None, "sem7_class6" : None, "sem7_class7" : None,
            "sem8_class1" : None, "sem8_class2" : None, "sem8_class3" : None, "sem8_class4" : None, "sem8_class5" : None, "sem8_class6" : None, "sem8_class7" : None, 
        }

        for key in semX_classY.keys():
            try:
                semX_classY[key] = request.data[key]
            except KeyError: 
                pass

        with connection.cursor() as cursor:
            # Gather Meta Info
            cursor.execute(queries[0], [request.data["map_name"]])
            cursor.execute(queries[1], [request.data["degree"].title()])
            cursor.execute(queries[2], [request.data["start_year"].upper()])
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
            cursor.execute(queries[11], [semX_classY["sem1_class1"]])
            cursor.execute(queries[12], [semX_classY["sem1_class2"]])
            cursor.execute(queries[13], [semX_classY["sem1_class3"]])
            cursor.execute(queries[14], [semX_classY["sem1_class4"]])
            cursor.execute(queries[15], [semX_classY["sem1_class5"]])
            cursor.execute(queries[16], [semX_classY["sem1_class6"]])
            cursor.execute(queries[17], [semX_classY["sem1_class7"]])
            cursor.execute(queries[18], [semX_classY["sem2_class1"]])
            cursor.execute(queries[19], [semX_classY["sem2_class2"]])
            cursor.execute(queries[20], [semX_classY["sem2_class3"]])
            cursor.execute(queries[21], [semX_classY["sem2_class4"]])
            cursor.execute(queries[22], [semX_classY["sem2_class5"]])
            cursor.execute(queries[23], [semX_classY["sem2_class6"]])
            cursor.execute(queries[24], [semX_classY["sem2_class7"]])
            cursor.execute(queries[25], [semX_classY["sem3_class1"]])
            cursor.execute(queries[26], [semX_classY["sem3_class2"]])
            cursor.execute(queries[27], [semX_classY["sem3_class3"]])
            cursor.execute(queries[28], [semX_classY["sem3_class4"]])
            cursor.execute(queries[29], [semX_classY["sem3_class5"]])
            cursor.execute(queries[30], [semX_classY["sem3_class6"]])
            cursor.execute(queries[31], [semX_classY["sem3_class7"]])
            cursor.execute(queries[32], [semX_classY["sem4_class1"]])
            cursor.execute(queries[33], [semX_classY["sem4_class2"]])
            cursor.execute(queries[34], [semX_classY["sem4_class3"]])
            cursor.execute(queries[35], [semX_classY["sem4_class4"]])
            cursor.execute(queries[36], [semX_classY["sem4_class5"]])
            cursor.execute(queries[37], [semX_classY["sem4_class6"]])
            cursor.execute(queries[38], [semX_classY["sem4_class7"]])
            cursor.execute(queries[39], [semX_classY["sem5_class1"]])
            cursor.execute(queries[40], [semX_classY["sem5_class2"]])
            cursor.execute(queries[41], [semX_classY["sem5_class3"]])
            cursor.execute(queries[42], [semX_classY["sem5_class4"]])
            cursor.execute(queries[43], [semX_classY["sem5_class5"]])
            cursor.execute(queries[44], [semX_classY["sem5_class6"]])
            cursor.execute(queries[45], [semX_classY["sem5_class7"]])
            cursor.execute(queries[46], [semX_classY["sem6_class1"]])
            cursor.execute(queries[47], [semX_classY["sem6_class2"]])
            cursor.execute(queries[48], [semX_classY["sem6_class3"]])
            cursor.execute(queries[49], [semX_classY["sem6_class4"]])
            cursor.execute(queries[50], [semX_classY["sem6_class5"]])
            cursor.execute(queries[51], [semX_classY["sem6_class6"]])
            cursor.execute(queries[52], [semX_classY["sem6_class7"]])
            cursor.execute(queries[53], [semX_classY["sem7_class1"]])
            cursor.execute(queries[54], [semX_classY["sem7_class2"]])
            cursor.execute(queries[55], [semX_classY["sem7_class3"]])
            cursor.execute(queries[56], [semX_classY["sem7_class4"]])
            cursor.execute(queries[57], [semX_classY["sem7_class5"]])
            cursor.execute(queries[58], [semX_classY["sem7_class6"]])
            cursor.execute(queries[59], [semX_classY["sem7_class7"]])
            cursor.execute(queries[60], [semX_classY["sem8_class1"]])
            cursor.execute(queries[61], [semX_classY["sem8_class2"]])
            cursor.execute(queries[62], [semX_classY["sem8_class3"]])
            cursor.execute(queries[63], [semX_classY["sem8_class4"]])
            cursor.execute(queries[64], [semX_classY["sem8_class5"]])
            cursor.execute(queries[65], [semX_classY["sem8_class6"]])
            cursor.execute(queries[66], [semX_classY["sem8_class7"]])

            # Insert courses into MAPS_DMAPS_LISTS
            cursor.execute(queries[67])

        map_id = get_latest_map_id()

        response = { 
            "message": "map successfully created.",
            "map_id" : map_id, 
        }

        return Response( response, status=status.HTTP_201_CREATED, content_type="application/json")


def get_latest_map_id():

    query = "SELECT MAX(map_id) FROM MAPS_DMAPS_META"

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    return result[0]

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