from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
from rest_framework import serializers


# class MapsCrsCatSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MapsCrseCatalog
#         fields = ['institute']

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['id','code','descr']

class CampDegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcadPlanTblLtd
        fields = ['degree_long_descr']