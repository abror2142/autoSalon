from rest_framework import serializers
from salon.models import Category, Car, Model
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    added_at = serializers.DateTimeField(read_only=True)
    parent_id = serializers.IntegerField(allow_null=True)
    
    def create(self, validated_data): 
        return Category.objects.create(**validated_data)


class CarSerializer(serializers.Serializer):
    model_id = serializers.IntegerField(allow_null=True)
    category_id = serializers.IntegerField(allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    mileage = serializers.IntegerField()
    year = serializers.IntegerField()
    color_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    

class ModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    company_id = serializers.IntegerField(allow_null=True)
    parent_id = serializers.IntegerField(allow_null=True)
    
    def create(self, validated_data):
        return Model.objects.create(**validated_data)



def serialization():
    category = Category.objects.get(pk=1)
    serializer = CategorySerializer(category)
    print(serializer.data)
    
    json = JSONRenderer().render(serializer.data)
    print(json)
    

def deserialization():
    json = b'{"name": "Moto", "parent_id": 1}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    
    serializer = CategorySerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    