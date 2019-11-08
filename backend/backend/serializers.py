from .models import MapsCrseCatalog, MapsInstitutions
from rest_framework import serializers


class MapsCrsCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsCrseCatalog
        fields = ['institute']

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['id','code','descr']