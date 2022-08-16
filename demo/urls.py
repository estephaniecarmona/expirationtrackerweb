from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path

from core.views import ProductList, ProductCreate



urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductList.as_view()),
    path('create/', ProductCreate.as_view())
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
