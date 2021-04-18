
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('gallery',views.gallery,name='gallery'),
    path('cart',views.cart,name='cart'),
    path('cart/signup',views.signup,name='signup'),
    path('cart/login',views.login,name='login'),
    path('cart2',views.cart2,name='cart2'),
    path('orders',views.orders,name='orders'),
]
