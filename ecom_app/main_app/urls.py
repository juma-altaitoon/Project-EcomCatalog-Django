from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('profile/', profile, name='users-profile'),

    # Product CRUD path
    path('product/', views.ProductList.as_view(), name ='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name= 'product_details'),
    path('product/create/', views.ProductCreate.as_view(), name= 'product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name = 'product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name = 'product_delete'),


]

