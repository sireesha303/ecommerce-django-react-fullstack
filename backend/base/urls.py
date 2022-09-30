
from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('products/', get_products_list),
    path('products/add/', add_product),
    path('products/<str:id>/', get_product_details),
    path('products/<str:id>/update/', update_product),
    path('products/<str:id>/delete/', delete_product),

    path('shipping-address/add/', add_shipping_address),
    path('shipping-address/<str:id>/', get_shipping_address),
    path('shipping-address/<str:id>/update/', update_shipping_address),

    path('orders/', get_user_orders),
    path('orders/add/', create_order),
    path('orders/<str:id>/', get_order_details),
    path('orders/<str:id>/update/', update_order),
    path('orders/<str:id>/delete/', delete_order),

    path('orders/<str:id>/order-items/', get_order_Items_list),
    path('orders/<str:id>/order-items/add/', add_order_item_to_order),
    # path('orders/<str:id>/order-items/<str:id>/delete/', delete_order_item),


    path('products/<str:id>/reviews/', get_product_reviews),
    path('products/<str:id>/reviews/add/', add_product_review),
    # path('products/<str:id>/reviews/<str:id>/delete/', delete_product_review),    #For Admin Purpose

    path('users/login/', MyTokenObtainPairView.as_view(), name='user login view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

