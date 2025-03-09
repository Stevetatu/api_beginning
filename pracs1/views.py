#from django.shortcuts import render
#from django.http import HttpResponse
from pracs1.models import Student
#from django.http import JsonResponse
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# All views that we take the urls
@api_view(['GET', 'POST'])
def studentview(request):
    if request.method == 'GET':
        # Get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

