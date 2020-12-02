from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Menu, Course
from .serializers import MenuSerializer, CourseSerializer

class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for Menus resource
    """
    queryset = Menu.objects.all().order_by('-id')
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.objects.all()
        not_empty = self.request.query_params.get('not_empty', None)
        if not_empty:
            queryset = Menu.objects.exclude(course=None)
        return queryset

    @action(detail=False)
    def count(self, request):
        count = self.filter_queryset(self.get_queryset()).count()
        content = {'count': count}
        return Response(content)

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for Courses resource
    """
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        queryset = Course.objects.all()
        menu = self.request.query_params.get('menu', None)
        if menu:
            queryset = Course.objects.filter(cards=menu)
        return queryset