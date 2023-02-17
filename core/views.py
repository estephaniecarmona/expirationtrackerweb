
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
from .forms import UserRegisterForm, ProductForm
from datetime import datetime, date, timedelta

from django.contrib.auth.models import User

from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin







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
        print(f'{productlistforuserid}productlistforuserid')

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
        print(filtered_products)
        if expirations == 'oldest':
            filtered_products = filtered_products.order_by('expiration')
        elif expirations == 'newest':
            filtered_products = filtered_products.order_by('-expiration')

        print(f'fp {filtered_products}')


      
        
  
        

        
        end_date = datetime.now().date() + timedelta(days=7)
      
         
        expiration_range = filtered_products.filter(expiration__lte=date.today())

        # print(f'exp_range{expiration_range}')
        if expired_products == 'expired':
            filtered_products = expiration_range
            print(filtered_products)
        elif expired_products == 'notexpired':
            filtered_products = filtered_products.filter(expiration__gte=date.today())




        print(len(expiration_range))



        form = self.form_class(initial={
            'category': categories, 
            'expiration': expirations,
            'expired_products': expired_products
        })  
           
    


        return render(request, 'core/product_list.html', {
            'form': form,
            'products': filtered_products,
            'expiration_count': len(expiration_range)
        })
    


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'name', 'date_purchased', 'expiration']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductEdit(UpdateView):
    model = Product
    fields = ['category', 'name', 'date_purchased', 'expiration']
    template_name_suffix = "_update_form"

class ProductDelete(DeleteView):
    model = Product

    success_url = '/product'

    # template_name = "product_confirm_delete.html"

