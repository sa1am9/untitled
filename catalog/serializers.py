from rest_framework import serializers
import time
from .models import Product

class ProductSerializer(serializers.Serializer):
    # pic = serializers.ImageField(allow_empty_file=True) # some errors with it
    name = serializers.CharField(max_length=256)
    created_date = serializers.DateTimeField()
    # borrower = serializers.CharField #and here errors
    color = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.crated_date = validated_data.get('created_date', instance.created_date)
        instance.color = validated_data.get('color', instance.color)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

