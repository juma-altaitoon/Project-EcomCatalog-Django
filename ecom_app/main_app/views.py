from django.shortcuts import render, redirect
from django.http import HttpResponse
# Import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return HttpResponse('<h1>Ecom App<h1>')