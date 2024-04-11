from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'shopapi'
urlpatterns = [
       path('shop/', ProductListAPIView.as_view(), name='api_shop_list'),
       path('shop/<int:pk>', ProductDetailAPIView.as_view(), name='api_shop_detail'),
       path('users/', UsersListAPIView.as_view(), name='api_users_list'),
       path('users/<int:pk>', UsersDetailAPIView.as_view(), name='api_users_detail'),
       path('upload_product/', ProductUploadAPIView.as_view(), name='api_shop_list'),
       path('<uuid:uuid>/comment', CommentAPIVeiw.as_view(), name='api_comment'),
       path('<uuid:uuid>/comment/<int:pid>', CommentAPIVeiw.as_view(), name='api_comment_of_parent'),

    
]