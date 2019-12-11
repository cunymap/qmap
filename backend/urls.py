"""DegreeMaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView
from . import views

from collections import OrderedDict

class DocsView(APIView):
    """
    Browsable REST API for DegreeMaps
    """
    #source: https://stackoverflow.com/questions/37066146/defaultrouter-class-not-creating-api-root-view-for-all-apps-in-python
    def get(self, request, *args, **kwargs):

        apidocs = [
                    ('Get a list of Campuses', request.build_absolute_uri('api/campuses/')),
                    ('Get a list of Degrees for a campus/institution', request.build_absolute_uri('api/degrees/17/')),
                    ('Get a course by course_id', request.build_absolute_uri('api/course/c000737/')),
                    ('Search courses by class name', request.build_absolute_uri('api/course/?q=355&id=17&major=computer%20science')),
                    ('Search courses by class description', request.build_absolute_uri('api/course/?q=Programming&id=17&major=computer%20science')),
                    ('Get a map by map_id', request.build_absolute_uri('api/map/2')),
                    ('Get the latest map', request.build_absolute_uri('api/map/?id=17&major=computer%20science&start_year=Fall%202020')),
                    ('Get Maps available for an Institution and Major', request.build_absolute_uri('api/map/?id=17&major=computer%20science')),
                ]

        apidocs = OrderedDict(apidocs)

        return Response(apidocs)

router = routers.DefaultRouter()

course_detail = views.Course.as_view({
    'get': 'retrieve',
})

course_search = views.Course.as_view({
    'get': 'search'
})

map = views.Map.as_view({
    'post': 'create_map',
    'get': 'map_by_institute_majorId'
})

maps_by_id = views.Map.as_view({
    'get': 'get_map_by_id',
    'delete': 'delete_map_by_id',
    'put': 'edit_map_by_id'
})

# map_by_institute_majorId = views.Map.as_view({
#     'get': 'map_by_institute_majorId'
# })

urlpatterns = [
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/campuses/', views.Campuses.as_view()),
    path('api/degrees/<int:id>/', views.Degrees.as_view()),
    path('api/course/', course_search, name='course_search'),
    path('api/course/<str:crse_id>/', course_detail, name='course_detail'),
    path('api/map/', map, name='map'),
    path('api/map/<str:map_id>/', maps_by_id, name='maps_by_id'),
    ]