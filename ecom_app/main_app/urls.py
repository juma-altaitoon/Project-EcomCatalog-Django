from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', profile, name='users-profile'),

]

