from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['id','code','descr']

class DegreesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcadPlanTblLtd
        fields = ['acad_plan', 'degree', 'degree_descr', 'degree_long_descr']