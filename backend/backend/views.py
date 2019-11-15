from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
from .serializers import CampusSerializer, DegreesSerializer

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

