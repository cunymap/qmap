from .models import *
from .serializers import *
from django.db import connection
import os
import json
from django.http import HttpResponse
import sqlparse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class Course(APIView):
    """
    API endpoint for courses in course catalog
    """
    def get(self, request, crse_id, format=None): #get a course by id
        serializer_context = {
            'request': request,
        }
        course = MapsCrseCatalog.objects.filter(course_id=crse_id)
        print(course.query)
        serializer = CourseSerializer(course, context=serializer_context, many=True)

        if course.exists():
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)


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
            result.append(dict(zip(keys,row)))

        json_data = json.dumps(result, indent=4)

        return HttpResponse(json_data, content_type="application/json")

def get_queries_from_file(filename):
    """ 
    Parses a sql file and returns sql queries as a list
    """

    with open(os.path.join('backend', 'queries', filename), 'r') as file:
        queryString = ""
        for line in file:
            if line.startswith("-"): #Skip comments    
                continue;
            else:
                queryString += line.replace('\n', ' ')
    queries = sqlparse.split(queryString)
   
    return queries
