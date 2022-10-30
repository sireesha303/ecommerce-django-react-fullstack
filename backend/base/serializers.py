from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


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


class UserSerializer(serializers.ModelSerializer):
    "user serializer"
    name = serializers.SerializerMethodField()
    isAdmin = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'name', 'isAdmin']

    def get_name(self, obj):
        if (obj.first_name != "") and (obj.last_name != ""):
            return obj.first_name+" "+obj.last_name
        else:
            return obj.username

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserCreateSerializer(UserSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Customized tokenpair view serializer """

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserCreateSerializer(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data
    #
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #
    #
    #     # token['name'] = user.username
    #
    #     return token




