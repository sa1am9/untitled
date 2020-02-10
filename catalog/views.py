from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        flowers = Product.objects.all()
        serializer = ProductSerializer(flowers, many=True)
        return Response({"flowers": serializer.data})

    def post(self, request):
        flowers = request.data.get('flowers')
        serializer = ProductSerializer(data=flowers)
        if serializer.is_valid(raise_exception=True):
            flowers_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(flowers_saved.name)})

# Create your views here.
