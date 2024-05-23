from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ResumeSerializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class Profile(APIView):
    def post(self, request, format=None):
        serializer = ResumeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage':'Profile Created Successfully','status':'success',
                             'candidate':serializer.data },status = status.HTTP_201_CREATED
                             )
        return Response(serializer.errors)
        
        

