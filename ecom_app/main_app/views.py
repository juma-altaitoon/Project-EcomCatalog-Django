from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Profile


# Create your views here.

@login_required
def profile(request):
    return render(request, 'users/profile.html')

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