from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
from rest_framework import viewsets
from .serializers import CampusSerializer, CampDegreeSerializer

"""
Create new view sets as classes in this file
"""

# class MapsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = MapsCrseCatalog.objects.all()[:10]
#     serializer_class = MapsCrsCatSerializer

class CampusView(viewsets.ModelViewSet):
    """
    API endpoint that outputs the name of all the campuses.
    """
    queryset = MapsInstitutions.objects.all()
    serializer_class = CampusSerializer

class camDegreeView(viewsets.ModelViewSet):
    """
    API endpoint that outputs the degrees offered in the campus selected.
    """
    camp = 'BAR01'
    queryset = AcadPlanTblLtd.objects.filter(institutecode =camp)
    serializer_class = CampDegreeSerializer