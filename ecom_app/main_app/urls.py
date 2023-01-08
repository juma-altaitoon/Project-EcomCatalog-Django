from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    path('profile/', profile, name='users-profile'),

]

