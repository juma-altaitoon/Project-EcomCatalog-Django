from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):

    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request,'about.html' )

def order(request):
    return render(request, 'order.html')

def checkout(request):
    return render(request, 'chekout.html')

def profile(request):
    return render(request, 'profile.html')

def products(request):
    return render(request, 'products.html')

# def collection(request):
#     return render(request, 'collection.html')

# def collections(request):
#     catagory = Catagory.objects.filter(status=0)
#     context = {'catagory': catagory}
#     return render(request, "main_app/products/collections.html", context)

# def CollectionsView(request, slug):
#     if (Category.objects.filter(slug=slug, status=0)):
#         products = Product.objects.filter(category__slug=slug)
#         context = {'products': products}
#         return render(request, "main_app/products/index.html")