
from cmath import exp
from tkinter import N
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from core.models import Product
from django.http import HttpResponse
from .forms import UserRegisterForm, ProductForm, Dateform
from datetime import datetime, date, timedelta

from django.contrib.auth.models import User

from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Product


# class Expirationcount(TemplateView):
#     template_name = 'base.html'
#     def get_context_data(self,*args, **kwargs):
#         context = super(Expirationcount), self).get_context_data(*args,**kwargs)
#         context['users'] = YourModel.objects.all()
#         return context

# class Expirationcount(TemplateView):
#     template_name = 'base.html'
#     extra_context = {'expiration_count': Product.objects.all()}



def get_expiration_count(self):
    productlistforuserid = self.model.objects.filter(user__id=self.request.user.id)
    filtered_products = productlistforuserid
    expiration_range = filtered_products.filter(expiration__lte=date.today())
    return len(expiration_range)

def index(request):
    return HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})    



def redirect_view(request):
    if request.user.is_authenticated:
        response = redirect('product/')
    else:
        response = redirect('home/')
    return response


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    form_class = ProductForm
    
    def get(self, request, *args, **kwargs):
        print(request.user.id)
        productlistforuserid = self.model.objects.filter(user__id=request.user.id)
        # print(f'{productlistforuserid}productlistforuserid')

        categories = self.request.GET.get('category')
        print(f'catergories{categories}')

        expirations = self.request.GET.get('expiration')

        expired_products = self.request.GET.get('expired_products')

        if categories is None:
            filtered_products = productlistforuserid
        elif categories == 'all':
            filtered_products = productlistforuserid
        else:
            filtered_products = productlistforuserid.filter(category__exact=categories)
        # print(filtered_products)
        if expirations == 'oldest':
            filtered_products = filtered_products.order_by('expiration')
        elif expirations == 'newest':
            filtered_products = filtered_products.order_by('-expiration')

        end_date = datetime.now().date() + timedelta(days=7)
      
         
        expiration_range = filtered_products.filter(expiration__lte=date.today())

        # print(f'exp_range{expiration_range}')
        if expired_products == 'expired':
            filtered_products = expiration_range
            print(filtered_products)
        elif expired_products == 'notexpired':
            filtered_products = filtered_products.filter(expiration__gte=date.today())




        # print(str(expiration_range))



        form = self.form_class(initial={
            'category': categories, 
            'expiration': expirations,
            'expired_products': expired_products
        })  
        
        context = {
            'form': form,
            'products': filtered_products,
            'expiration_count': get_expiration_count(self)
        }
        return render(request, 'core/product_list.html', context)
    


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    success_url = '/'

    form_class = Dateform

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreate, self).get_context_data(*args, **kwargs)
        context['expiration_count'] = get_expiration_count(self)
        return context
    

class ProductEdit(UpdateView):
    model = Product
    fields = ['category', 'name', 'date_purchased', 'expiration']
    template_name_suffix = "_update_form"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductEdit, self).get_context_data(*args, **kwargs)
        context['expiration_count'] = get_expiration_count(self)
        return context


class ProductDelete(DeleteView):
    model = Product
    success_url = '/product'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDelete, self).get_context_data(*args, **kwargs)
        context['expiration_count'] = get_expiration_count(self)
        return  context
    
# class Login(LoginView):
#     model = Product
#     success_url = '/'

#     def get_context_data(self, *args, **kwargs):
#         context = super(LoginView, self).get_context_data(*args, **kwargs)
#         context['expiration_count'] = get_expiration_count(self)
#         return  context

