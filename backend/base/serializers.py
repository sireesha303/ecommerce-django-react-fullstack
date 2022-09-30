from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class OrderItemSerializer(serializers.ModelSerializer):
    """OrderItem Serializer"""
    class Meta:
        model = OrderItem
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Review Serializer"""
    class Meta:
        model = Review
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     "user serializer"
#     name = serializers.SerializerMethodField()
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_superuser','name']
#
#     def get_name(self, obj):
#         if (obj.first_name != None) and (obj.last_name != None):
#             return obj.first_name+" "+obj.last_name
#         else:
#             return obj.username


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Customized tokenpair view serializer """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username

        return token

