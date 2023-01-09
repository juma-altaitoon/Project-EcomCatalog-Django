from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category


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

#  Product CRUD
class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', ]

class ProductDelete(DeleteView):
    model = Product
    success_url = '/product/'


# Category CRUD
class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/category/'
