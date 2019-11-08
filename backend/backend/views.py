from .models import MapsCrseCatalog, MapsInstitutions
from rest_framework import viewsets
from .serializers import CampusSerializer

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
    API endpoint the outputs the name of all the campuses.
    """
    queryset = MapsInstitutions.objects.all()
    serializer_class = CampusSerializer
