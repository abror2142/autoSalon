from rest_framework import serializers
from salon.models import Category, Car, Model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'