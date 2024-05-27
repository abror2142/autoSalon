from django.shortcuts import render
from .serializers import CategorySerializer, CarSerializer, ModelSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from salon.models import Category, Car, Model
from rest_framework.views import APIView
from rest_framework.response import Response


# class CarList(ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# class CarCreate(CreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


class CarListCreate(APIView):
    
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        data = serializer.data
        return Response(data)
    
    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error')
    


class CarDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CategoryList(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryListCreate(APIView):
    
    def get(self, request):
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error, Not created')


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ModelList(ListAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer


class ModelListCreate(APIView):
    
    def get(self, request):
        data = Model.objects.all()
        serializer = ModelSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ModelSerializer(data=data)
     
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        print(serializer.data)
        return Response('Error, Not created')


class ModelDetail(RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

