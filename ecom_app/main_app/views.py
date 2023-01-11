from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q 

# Create your views here.

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')

def home(request):

    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request,'about.html' )

def order(request):
    return render(request, 'order.html')

def chekout(request):
    return render(request, 'chekout.html')

def policy(request):
    return render(request, 'policy.html')

#  Product CRUD
class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', 'image' ,'sku', 'category']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', ]

class ProductDelete(DeleteView):
    model = Product
    success_url = '/product/'

def signup(request):
    error_message = ""
    #error message is a must for project 3
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid attempt - Try again."
    
    form = UserCreationForm()
    context = {'form': form, ' error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Category CRUD
class CategoryList(ListView):
    model = Category
    
class CategoryDetail(DetailView):
    model = Category

    # def get_queryset(self, *args, **kwargs):
        
    #     product_list = Product.objects.filter()
    #     return product_list


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/category/'

# class CategoryProductListView(ListView):
#     template_name = 'products_by_category'
#     model = Product
#     def get_queryset(self):   
#         query = self.request.GET.get("pk")
#         Product.objects.filter(Q(category__icontains = query))

class SearchResultView(ListView):
    model= Product
    template_name = 'search_result'

    def get_queryset(self):
        result = self.request.GET.get("search")
        object_list = Product.objects.filter(
            Q(name__icontains = result)
        )
        return object_list

# class CategoyByUserView(ListView):
#     model= Category
#     template_name = 'category_user'

#     def get_queryset(self):
#         object_list = Category.objects.filter(user= self.request.user)
#         return object_list
# class ProductByUserView(ListView):
#     model= Product
#     template_name = 'product_user'

#     def get_queryset(self):
#         object_list =Product.objects.filter(user= self.request.user)
#         return object_list
def dashboard(request):
    return render(request, 'dashboard.html')