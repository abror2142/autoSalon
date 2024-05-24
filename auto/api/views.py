from django.shortcuts import render
from .serializers import CategorySerializer, CarSerializer, ModelSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from salon.models import Category, Car, Model


class CarList(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreate(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModelList(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelDetail(RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

