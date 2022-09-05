
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from core.models import Product
from django.http import HttpResponse
from .forms import UserRegisterForm


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
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


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

