from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from .models import Product, Profile

=======
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
>>>>>>> 92092d1e19108009137a50a4d4c0d61f170fa38e

# Create your views here.

@login_required
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
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', ]

class ProductDelete(DeleteView):
    model = Product
    success_url = '/product/'

<<<<<<< HEAD
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['name', 'last_name', 'roles', 'date', 'avatar','bio' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar', 'bio']

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = '/profiles/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profiles_index(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/index.html', {'profiles': profiles})

@login_required
def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    products_profile_doesnt_have = Product.objects.exclude(id__in = profile.products.all().values_list('id'))
    return render(request, 'profiles/detail.html', {'profile': profile, 'products': products_profile_doesnt_have})

def signup(request):
    error_message = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = "Invalid signup - Please try again later"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context )
=======
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

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/category/'

class CategoryProductListView(ListView):
    template_name = 'products_by_category'

    def get_queryset(self):        
        query = self.request.GET.get("pk")
        Product.objects.filter(Q(category__icontains = query))

class SearchResultView(ListView):
    model= Product
    template_name = 'search_result'

    def get_queryset(self):
        result = self.request.GET.get("search")
        object_list = Product.objects.filter(
            Q(name__icontains = result)
        )
        return object_list
>>>>>>> 92092d1e19108009137a50a4d4c0d61f170fa38e
