from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.http import Http404


@api_view(['GET'])
def get_products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, id):
    try:
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    except Product.DoesNotExist:
        raise Http404


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Product.DoesNotExist:
        raise Http404


@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response("product Deleted Successfully!..")

