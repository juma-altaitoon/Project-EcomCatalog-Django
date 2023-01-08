from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request,'about.html' )

def order(request):
    return render(request, 'order.html')
