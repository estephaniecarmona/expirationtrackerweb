from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.views.generic.dates import DateDetailView
from core.views import ProductList, ProductCreate, ProductEdit, ProductDelete
from core.views import redirect_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductList.as_view()),
    path('create/', ProductCreate.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductEdit.as_view(), name="product-update" ),
    path('<int:pk>/delete/', ProductDelete.as_view(), name="product-delete"),
    path('/redirect/', redirect_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
