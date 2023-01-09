from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.order, name='profile'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('main_app/users/', views.profile, name='profile'),
    path('products/products/', views.products, name='products'),
]
