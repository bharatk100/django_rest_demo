from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView #APIView is used to normal view can writen api data
from rest_framework.response import Response
from rest_framework import status

from . models import employee
from . serializers import employeeSerializer


#cls based view inherit from APIView

class employeeList(APIView):

    def get(self, request):
        employees=employee.objects.all()
        serializer=employeeSerializer(employees, many=True) # all objects convert them into JSON
        return Response(serializer.data)

    def post(self):
        pass




