from django.shortcuts import render,redirect,HttpResponseRedirect
from .serializer import ReviewSerializers,CourseEnrlSerializer,MostFavoriteCourseSerializer
from .models import ReviewModel,CourseEnrolModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from course.models import CourseModel
from course.serializers import CourseSerializer
from django.contrib.auth.models import User
from account.models import UserRegistrarionModel
import operator
from django.db.models import Q
from sslcommerz_lib import SSLCOMMERZ

# Create your views here.

class AllReviewView(viewsets.ViewSet):
    def list(self,request):
        data = []
        reviews = ReviewModel.objects.all()
        serializer = ReviewSerializers(reviews,many=True)
        for sr in serializer.data:
            get_data = {}
            try:
                user = User.objects.get(pk=sr['reviewer'])
                image = UserRegistrarionModel.objects.get(user=user)
                get_data['name'] = f'{user.first_name} {user.last_name}'
                get_data['image'] = str(image.image)
                get_data['review']=sr['review']
                get_data['rating']=sr['rating']
                get_data['date']=sr['date']

                # print(get_data)
                data.append(get_data)
            except(User.DoesNotExist):
                return Response({'error':"bad request"})
        return Response({'data':data})

class ReviewView(viewsets.ViewSet):
    # permission_classes=[IsAuthenticated]
    def list(self,request,course_id):
        data = []
        reviews = ReviewModel.objects.filter(course=course_id)
        serializer = ReviewSerializers(reviews,many=True)
        for sr in serializer.data:
            get_data = {}
            try:
                user = User.objects.get(pk=sr['reviewer'])
                image = UserRegistrarionModel.objects.get(user=user)
                get_data['name'] = f'{user.first_name} {user.last_name}'
                get_data['image'] = str(image.image)
                get_data['review']=sr['review']
                get_data['rating']=sr['rating']
                get_data['date']=sr['date']

                # print(get_data)
                data.append(get_data)
            except(User.DoesNotExist):
                return Response({'error':"bad request"})
        return Response({'data':data})
    

    def create(self,request):
        serializer = ReviewSerializers(data = request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"comment push successfully"})
        print(serializer.errors)
        return Response({"error":"Something wrong please try agin"})
        

class CourseEnrolView(viewsets.ViewSet):
    # permission_classes=[IsAuthenticated]
    
    def list(self,request,enrol_by):
        courses=CourseEnrolModel.objects.filter(enrol_by=enrol_by)
        # data = {enroled_courses.enrol_course.title,enroled_courses.enrol_course.price,enroled_courses.date}
        serializer =CourseEnrlSerializer(courses,many=True)
        course_details = []
        for cr in serializer.data:
            print(cr['enrol_course'])
            try:
                course = CourseModel.objects.get(pk=cr['enrol_course'])
                sr = CourseSerializer(course)
                data = {}
                data
                data['title']=sr.data['title']
                data['price']=sr.data['price']
                data['course_duration']=sr.data['course_duration']
                course_details.append(data)
            except(CourseModel.DoesNotExist):
                course = None
        return Response({"data":serializer.data,"course_details":course_details})

    def create(self,request):

        courseNo = request.data['enrol_course']
        enrolBy = request.data['enrol_by']
        try:
            is_enroled = CourseEnrolModel.objects.filter(enrol_course=courseNo,enrol_by=enrolBy)
        except(CourseEnrolModel.DoesNotExist):
            is_enroled=False
        print(is_enroled)
        if not is_enroled:
            serializer =CourseEnrlSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"msg":"Already enroled this course"})
    def destroy(self,request,id):
        try:
            course = CourseEnrolModel.objects.get(pk=id)
            course.delete()
            return Response({'success':'Course Unenrolled successfully'})
        except(CourseEnrolModel.DoesNotExist):
            course=None
            return Response({'error':'Operation Failed'})


class FavoriteCourseView(viewsets.ViewSet):
    def list(self,request):
        dictionary = {}
        data  = {}
        data_list=[]
        query = ReviewModel.objects.all()
        for q in query:
            if(q.course.pk in dictionary.keys()): 
                dictionary[q.course.pk]+=int(q.rating)
                continue
            dictionary[q.course.pk]=int(q.rating)
        serializer = MostFavoriteCourseSerializer(query,many=True)
        
        for d in serializer.data:
            if(d['id'] in data.keys()): continue
            d['ratting']=dictionary[d['id']]
            data[d['id']]=d
            data_list.append(d)
        data_list=sorted(data_list, key=lambda x:x['ratting'],reverse=True)[:4]

        return Response(data_list)


class MyStudentsViews(viewsets.ViewSet):
    def list(self,request,userId):
        students_id = []
        student_list = []
        courses = CourseEnrolModel.objects.all()
        
        for course in courses:
            if((course.enrol_course.user.pk==int(userId)) and (course.enrol_by.pk not in students_id)):
                students_id.append(course.enrol_by.pk)
        print(User.objects.get(pk=int(students_id[0])))
        for student in student_list:
            query = User.objects.get(pk=int(student))
            print(query)
            student_list.append(query)
        print(students_id)
        print(student_list)

        return Response({"data":student_list})


def PaymentMethodIntegration(request):
    print('Hello')
    print(request.user)
    settings = { 'store_id': 'jsrns671f12dd2f84d', 'store_pass': 'jsrns671f12dd2f84d@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "https://46ra20.github.io/DRF_FrontEnd/myLearing.html"
    post_body['fail_url'] = "https://46ra20.github.io/DRF_FrontEnd/myLearing.html"
    post_body['cancel_url'] = "https://46ra20.github.io/DRF_FrontEnd/myLearing.html"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    return redirect(response['GatewayPageURL'])
