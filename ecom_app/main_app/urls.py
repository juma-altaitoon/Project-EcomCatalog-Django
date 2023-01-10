from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.home, name='home'),
    # path('profile/', views.order, name='profile'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('chekout/', views.chekout, name='checkout'),
    path('profile/', views.profile, name='users-profile'),
    path('policy/', views.policy, name='policy'),


    # Product CRUD path
    path('product/', views.ProductList.as_view(), name ='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name= 'product_details'),
    path('product/create/', views.ProductCreate.as_view(), name= 'product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name = 'product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name = 'product_delete'),

    path('main_app/users/', views.profile, name='profile'),
       
    
       
        #Sign-up
    path('accouts/signup/', views.signup, name='signup'),

    # Category CRUD path
    path('category/', views.CategoryList.as_view(), name ='category'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name= 'category_details'),
    path('category/create/', views.CategoryCreate.as_view(), name= 'category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name = 'category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name = 'category_delete'),
    # Products by Category
    path('product/<category>/', views.CategoryProductListView.as_view(), name = 'product_by_category'),
    # Search path
    path('search/', views.SearchResultView.as_view(), name = 'search_result'),

]

