
from .views import *
from django.urls import path

urlpatterns = [
    path('products/', get_products_list),
    path('products/add/', add_product),
    path('products/<str:id>/', get_product_details),
    path('products/<str:id>/update/', update_product),
    path('products/<str:id>/delete/', delete_product),
]