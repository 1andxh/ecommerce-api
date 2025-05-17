from django.urls import path
from orders import views

urlpatterns = [
    path('orders/', views.order_list),
    # path('products/<int:pk>/', views.product_detail)
]