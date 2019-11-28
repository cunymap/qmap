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

# class MapsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = MapsCrseCatalog.objects.all()[:10]
#     serializer_class = MapsCrsCatSerializer

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
    def get(self, request, code, format=None):
        degrees = AcadPlanTblLtd.objects.filter(institutecode=code)
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
        keys = ('course_id', 'eff_date', 'institute_id', 'status', 'subject', 'catalog', 'descr', 'min_units', 'max_units', 'designnation')

        for row in rows:
            result.append(OrderedDict(zip(keys,row)))

        if(len(result) == 0):
            return Response({ 'message': 'No matching courses found' }, status=status.HTTP_200_OK)
        
        else:
            json_data = json.dumps(result, indent=4, default=str)
            return HttpResponse(json_data, content_type="application/json")


class Map(APIView):
    """
    Return all maps for a particular institution and major
    """
    def get(self, request, map_id, format=None):
        # Get and execute query from file
        queries = get_queries_from_file("returnMapsInfo.sql")

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

def get_queries_from_file(filename):
    """ 
    Parses a sql file and returns sql queries as a list
    """

    with open(os.path.join('backend', 'queries', filename), 'r') as file:

        # Skip initial comments that starts with #
        while True:
            line = file.readline()
            # break while statement if it is not a comment line
            # i.e. does not startwith #
            if not line.startswith('-'):
                break

        # Second while loop to process the rest of the file
        queryString = ""
        while line:
            # queryString += line.replace('\n', ' ')
            queryString += line
            line = file.readline()

    queries = sqlparse.split(queryString)
   
    return queries