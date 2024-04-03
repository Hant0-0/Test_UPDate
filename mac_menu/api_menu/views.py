from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api_menu.models import Product
from api_menu.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(APIView):
    def get(self, request, title):
        product = get_object_or_404(Product, title=title)
        serializer = ProductSerializer(product).data
        return Response(serializer, status=status.HTTP_200_OK)


class ProductDetailFieldDetailAPIView(APIView):
    def get(self, request, title, field):
        product = get_object_or_404(Product, title=title)
        serializer = ProductSerializer(product).data
        return Response({field: serializer[field]}, status=status.HTTP_200_OK)