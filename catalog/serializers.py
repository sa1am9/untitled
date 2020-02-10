from rest_framework import serializers
import time
from .models import Product

class ProductSerializer(serializers.Serializer):
    # pic = serializers.ImageField(allow_empty_file=True)
    name = serializers.CharField(max_length=256)
    created_date = serializers.DateTimeField()
    # borrower = serializers.CharField()
    color = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)