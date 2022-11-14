from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.views.generic.dates import DateDetailView
from core.views import ProductList, ProductCreate, ProductEdit, ProductDelete, redirect_view, register
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView





LOGIN_REDIRECT_URL = "/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),


    # path('', TemplateView.as_view,
    path('', redirect_view),

    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    path('product/', ProductList.as_view(), name="home"),
    path('create/', ProductCreate.as_view(), name="product-create"),
    path('<int:pk>/update/', ProductEdit.as_view(), name="product-update"),
    path('<int:pk>/delete/', ProductDelete.as_view(), name="product-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
