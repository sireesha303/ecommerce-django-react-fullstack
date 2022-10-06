from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated


@api_view(['GET'])
def get_products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, id):
    try:
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        raise Http404


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
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
@permission_classes([IsAdminUser])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response("product Deleted Successfully!..")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_shipping_address(request):
    serializer = ShippingAddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_shipping_address(request, id):
    try:
        address = ShippingAddress.objects.get(id=id)
        serializer = ShippingAddressSerializer(instance=address, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except ShippingAddress.DoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_shipping_address(request, id):
    try:
        shippingaddress = ShippingAddress.objects.get(id=id)
        serializer = ShippingAddressSerializer(shippingaddress, many=False)
        return Response(serializer.data)
    except ShippingAddress.DoesNotExist:
        raise Http404


# class PostListGenericView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_details(request, id):
    try:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    except Order.DoesNotExist:
        raise Http404


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_order(request, id):
    try:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Order.DoesNotExist:
        raise Http404


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return Response("order Deleted Successfully!..")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_Items_list(request, order_id):
    order_itmes = OrderItem.objects.filter(order__id=order_id)
    serializer = OrderItemSerializer(order_itmes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order_item_to_order(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order_item(request, id):
    order_item = OrderItem.objects.get(id=id)
    order_item.delete()
    return Response("order Deleted Successfully!..")


@api_view(['GET'])
def get_product_reviews(request, product_id):
    reviews = Review.objects.filter(product__id=product_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return Response("review Deleted Successfully!..")


class MyTokenObtainPairView(TokenObtainPairView):
    """ Customized tokenpair view """
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


