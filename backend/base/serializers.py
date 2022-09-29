from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""
    class Meta:
        model = Product
        fields = "__all__"

