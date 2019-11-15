from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd
from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['id','code','descr']

<<<<<<< HEAD
class CampDegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcadPlanTblLtd
        fields = ['degree_long_descr']
=======
class MajorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcadPlanTblLtd
        fields = ['acad_plan', 'degree', 'degree_descr', 'degree_long_descr']
>>>>>>> b923e761c216aa4ab8d396cd04dc46fa9576613d
