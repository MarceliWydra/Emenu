from django.db.models import Count
from rest_framework import serializers
from .models import Course, Menu

class MenuSerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField(source='course_set.count', read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Course
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        url = obj.image.name
        return url
