from .models import MapsCrseCatalog, MapsInstitutions, AcadPlanTblLtd, MapsDmapsLists
from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['id','code','descr']

class DegreesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcadPlanTblLtd
        fields = ['acad_plan', 'degree', 'degree_descr', 'degree_long_descr']

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsDmapsLists
        fields = ['map', 'semester_num', 'course1', 'course2', 'course3', 'course4', 'course5', 'course6', 'course7']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsCrseCatalog
        fields = ['course_id', 'eff_date', 'status', 'subject', 'catalog', 'descr', 'min_units', 'max_units', 'designation']

