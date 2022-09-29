from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""
    class Meta:
        model = Product
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    """ShippingAddress Serializer"""
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """ShippingAddress Serializer"""
    class Meta:
        model = Order
        fields = "__all__"


