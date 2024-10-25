from rest_framework import serializers
from .models import ReviewModel,CourseEnrolModel,User
from course.models import CourseModel

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class CourseEnrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrolModel
        fields='__all__'

class MostFavoriteCourseSerializer(serializers.ModelSerializer):
    title=serializers.CharField(source='course.title')
    image = serializers.CharField(source='course.image')
    ratting = 5
    price = serializers.DecimalField(source='course.price',max_digits=12,decimal_places=2)
    id = serializers.IntegerField(source='course.pk')
    class Meta:
        model = ReviewModel
        fields=['title','image','price','id']
