from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static

from django.conf import settings

app_name = 'shop'

urlpatterns = [
   
   path('', ProductList.as_view(), name='shop_list'),
   path('create/', update.as_view(), name='up'),
   path('<int:pk>', ProductDetail.as_view(), name='shop_detail'),
    
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)