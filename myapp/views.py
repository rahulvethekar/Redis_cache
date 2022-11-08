from re import S
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.

class StudentView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # @method_decorator(cache_page(60*1))
    def get(self,request):
        data = request.data
        Student_data = Student.objects.all()
        serializer = StudentSerializer(Student_data,many = True)
        return Response(serializer.data)




