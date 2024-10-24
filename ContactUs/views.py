from django.shortcuts import render
from .models import ContactUs
from .serializer import ContactUsSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.

class ContactUsView(ViewSet):
    def create(self,request):
        serializer = ContactUsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'We will contact yourself'})
        return Response({'message':'Try again later'})
