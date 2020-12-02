from django.contrib import admin
from .models import Course, Menu


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Course, CourseAdmin)
