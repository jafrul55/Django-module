from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

class StudentView(APIView):
    def get(self, request,):
        student_data = models.StudentData.objects.all()
        serializer = serializers.StudentSerializers(student_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
    def get(self, request, pk, format=None):
        student_data = models.StudentData.objects.get(pk=pk)
        serializer = serializers.StudentSerializers(student_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student_data = models.StudentData.objects.get(pk=pk)
        serializer = serializers.StudentSerializers(student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student_data = models.StudentData.objects.get(pk=pk)
        student_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)