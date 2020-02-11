from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from rest_framework.generics import get_object_or_404
from .serializers import ProductSerializer

class ProductView(APIView):

    def get(self, request):
        '''
        Get all items.
        '''
        flowers = Product.objects.all()
        serializer = ProductSerializer(flowers, many=True)
        return Response({"flowers": serializer.data})

    def post(self, request):
        '''
        Create a new item.
        '''
        flowers = request.data.get('flowers')
        serializer = ProductSerializer(data=flowers)
        if serializer.is_valid(raise_exception=True):
            flowers_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(flowers_saved.name)})

    def put(self, request, pk):
        '''
        Change item by id.
        '''
        saved_flower = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('catalog')
        serializer = ProductSerializer(instance=saved_flower, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            flower_saved = serializer.save()
        return Response({
            "success": "Flower '{}' updated successfully".format(flower_saved.name)})

    def delete(self, request, pk):
        '''
        Delete item by id.
        '''
        flower = get_object_or_404(Product.objects.all(), pk=pk)
        flower.delete()
        return Response({"message":"Flower with id {} has been deleted".format(pk)}, status=204)