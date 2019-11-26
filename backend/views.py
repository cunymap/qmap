from .models import *
from .serializers import *
from django.db import connection
import os
import json
from django.http import HttpResponse


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

        with open(os.path.join('backend', 'queries', 'returnMapsInfo.sql'), 'r') as file:
            queryString = file.read().replace('\n', ' ')

        cursor = connection.cursor()
        cursor.execute("SET @map_id=%s;", [map_id])
        cursor.execute(queryString)
        rows = cursor.fetchall()
        result = []
        keys = ('map_id','semester_num','course_id', 'subject', 'catalog', 'descr', 'min_units', 'max_units', 'designation')
        for row in rows:
            result.append(dict(zip(keys,row)))
        json_data = json.dumps(result, indent=4)

        return HttpResponse(json_data, content_type="application/json")


