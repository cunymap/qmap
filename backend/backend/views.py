from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
<<<<<<< HEAD
from rest_framework import viewsets
from .serializers import CampusSerializer, CampDegreeSerializer
=======
from .serializers import CampusSerializer, MajorsSerializer
>>>>>>> b923e761c216aa4ab8d396cd04dc46fa9576613d

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
<<<<<<< HEAD
    queryset = MapsInstitutions.objects.all()
    serializer_class = CampusSerializer

class camDegreeView(viewsets.ModelViewSet):
    """
    API endpoint that outputs the degrees offered in the campus selected.
    """
    camp = 'BAR01'
    queryset = AcadPlanTblLtd.objects.filter(institutecode =camp)
    serializer_class = CampDegreeSerializer
=======
    def get(self, request, format=None):
        campuses = MapsInstitutions.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)

class Majors(APIView):
    """
    API endpoint that outputs the name of all the majors for a particular campus.
    """
    def get(self, request, code, format=None):
        majors = AcadPlanTblLtd.objects.filter(institutecode=code)
        serializer = MajorsSerializer(majors, many=True)

        if majors.exists():
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

>>>>>>> b923e761c216aa4ab8d396cd04dc46fa9576613d
