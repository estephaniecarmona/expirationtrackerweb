
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

from django.utils import timezone









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
    response = redirect('/redirect-success/')
    return response


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    form_class = ProductForm

    def get(self, request, *args, **kwargs):
   
        categories = self.request.GET.get('category')
        form = self.form_class()  
           

        expirations = self.request.GET.get('expiration')

        expired_products = self.request.GET.get('expired_products')



        

        
        

        
        if categories is None:
            filtered_products = self.model.objects.all()
        elif categories == 'all':
            filtered_products = self.model.objects.all()
            
        else:
            filtered_products = self.model.objects.filter(category__exact=categories)
        print(filtered_products)
        if expirations == 'oldest':
            filtered_products = filtered_products.order_by('expiration')
        elif expirations == 'newest':
            filtered_products = filtered_products.order_by('-expiration')

        print(f'fp {filtered_products}')


      
        
  
        

        
        end_date = datetime.now().date() + timedelta(days=7)
      
        # expiration_range = self.model.object.filter(expiration__lte=date.today())   
        expiration_range = filtered_products.filter(expiration__lte=date.today())

        print(f'exp_range{expiration_range}')
        if expired_products == 'expired':
            filtered_products = expiration_range
            print(filtered_products)
        elif expired_products == 'notexpired':
            filtered_products = filtered_products.filter(expiration__gte=date.today())




        print(len(expiration_range))
    


        return render(request, 'core/product_list.html', {'form': form, 'products': filtered_products, 'expiration_count': len(expiration_range)})
    
    





    # def get(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(ProductList, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class ProductCreate(CreateView):
    model = Product
    fields = ['category', 'name', 'date_purchased', 'expiration']
    success_url = '/'
    


class ProductEdit(UpdateView):
    model = Product
    fields = ['category', 'name', 'date_purchased', 'expiration']
    template_name_suffix = "_update_form"

class ProductDelete(DeleteView):
    model = Product

    success_url = '/product'

    # template_name = "product_confirm_delete.html"

