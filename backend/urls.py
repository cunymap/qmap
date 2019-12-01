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
                    ('Campuses', request.build_absolute_uri('api/campuses/')),
                    ('Degrees', request.build_absolute_uri('api/degrees/17/')),
                    ('Course', request.build_absolute_uri('api/course/c000737/')),
                    ('CourseSearchByClassName', request.build_absolute_uri('api/course/?q=355&id=17&major=computer%20science')),
                    ('CourseSearchByClassDescription', request.build_absolute_uri('api/course/?q=Programming&id=17&major=computer%20science')),
                    ('Map', request.build_absolute_uri('api/map/2')),
                ]

        apidocs = OrderedDict(apidocs)

        return Response(apidocs)

router = routers.DefaultRouter()

course_detail = views.Course.as_view({
    'get': 'retrieve'
})

course_search = views.Course.as_view({
    'get': 'search'
})

urlpatterns = [
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/campuses/', views.Campuses.as_view()),
    path('api/degrees/<int:id>/', views.Degrees.as_view()),
    path('api/course/', course_search, name='course_search'),
    path('api/course/<str:crse_id>/', course_detail, name='course_detail'),
    path('api/map/<str:map_id>/', views.Map.as_view()),
    ]