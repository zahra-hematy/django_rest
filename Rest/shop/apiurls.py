from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
app_name = 'shopapi'


router = routers.SimpleRouter()
# router.register('shop', ProductListAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ProductListAPIView.as_view(), name='api_shop_list'),
    path('shop/<int:pk>', ProductDetailAPIView.as_view(), name='api_shop_detail'),
    path('users/', UsersListAPIView.as_view(), name='api_users_list'),
    path('users/<int:pk>', UsersDetailAPIView.as_view(), name='api_users_detail'),
]



# urlpatterns = [
       # path('shop/', ProductListAPIView.as_view(), name='api_shop_list'),
       # path('shop/<int:pk>', ProductDetailAPIView.as_view(), name='api_shop_detail'),
       # path('users/', UsersListAPIView.as_view(), name='api_users_list'),
       # path('users/<int:pk>', UsersDetailAPIView.as_view(), name='api_users_detail'),
#        path('upload_product/', ProductUploadAPIView.as_view(), name='api_shop_list'),
#        path('<uuid:uuid>/comment', CommentAPIVeiw.as_view(), name='api_comment'),
#        path('<uuid:uuid>/comment/<int:pid>', CommentAPIVeiw.as_view(), name='api_comment_of_parent'),

# ]