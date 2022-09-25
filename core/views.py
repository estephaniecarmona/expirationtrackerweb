# from nis import cat
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from core.models import Product
from django.http import HttpResponse
from .forms import UserRegisterForm, ProductForm


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

        
        if categories is None:
            filtered_products = self.model.objects.all()
        elif categories == 'all':
            filtered_products = self.model.objects.all()
            print(filtered_products)
        else:
            filtered_products = self.model.objects.filter(category__exact=categories)

        if expirations == 'oldest':
            filtered_products = filtered_products.order_by('expiration')
        elif expirations == 'newest':
            filtered_products = filtered_products.order_by('-expiration')
        

        return render(request, 'core/product_list.html', {'form': form, 'products': filtered_products})
    





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

