from django.contrib import admin
from .models import ReviewModel,CourseEnrolModel
# from models import Review
# Register your models here.

class AdminTable(admin.ModelAdmin):
    list_display=['reviewer','review','rating','course_title','date']

    def get_reviewer(self,obj):
        return obj.user
    def course_title(self,obj):
        return obj.course.title

admin.site.register(ReviewModel,AdminTable)
admin.site.register(CourseEnrolModel)
