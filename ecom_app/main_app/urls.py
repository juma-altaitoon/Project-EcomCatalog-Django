from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/products/', views.products, name='products'),
    path('profile/', profile, name='users-profile'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profiles_delete'),

    # Product CRUD path
    path('product/', views.ProductList.as_view(), name ='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name= 'product_details'),
    path('product/create/', views.ProductCreate.as_view(), name= 'product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name = 'product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name = 'product_delete'),


    path('accounts/signup/', views.signup, name='signup')


]

