from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView # Http verb like get, put, post
from rest_framework.generics import(
     ListAPIView,
     ListCreateAPIView,
     CreateAPIView,
     DestroyAPIView,
     UpdateAPIView,
     RetrieveAPIView,
     RetrieveDestroyAPIView,
     RetrieveUpdateAPIView,
     RetrieveUpdateDestroyAPIView,
)
       
from rest_framework.viewsets import ModelViewSet  #action CRUDE
from . import serializers
from rest_framework.response import Response
from .models import *
from django.views import generic
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.views.generic import ListView, DetailView, DeleteView, RedirectView
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
import uuid 
import os
from .permissions import *
from datetime import datetime
from rest_framework import filters
from .filters import *
User = get_user_model()

class ProductList(ListView):
    def get_queryset(self):
        return Product.objects.filter(status='availble')
class ProductDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Product.objects.filter(status='availble'),
            pk = self.kwargs.get('pk')
        )


# class ProductListAPIView(APIView):  # custom api
#     permission_classes = [IsAdminUser, IsAuthorOrReadOnly]
#     def get(self, request, format=None, *args, **kwargs): 
#         product = Product.objects.all()
#         s = serializers.ProductSerializer(product, many=True)
#         return Response(s.data)
# User = get_user_model()

# from rest_framework import serializers as s

class ProductListAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.all()   

    # User = s.PrimaryKeyRelatedField(many=True, read_only=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsStaffOrReadOnly,)
    filterset_fields = [ 'name', 'user', 'color' ]  # create a box with these as its feilds
    ordering = ['status'] # default ordering
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description'] # create a search box
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['name', 'description']
    # filter_backends = [IsOwnerFilterBackend]

    

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(status='availble')
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    filter_backends = [IsOwnerFilterBackend]



class UsersListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsSuperuserOrReadOnly,)
class UsersDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthorOrReadOnly, IsSuperuserOrReadOnly)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        perms = [item.codename for item in (Permission.objects.filter(user=user) | Permission.objects.filter(group__user=user))]
        token['perms'] = perms
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProductUploadAPIView(CreateAPIView):
    serializer_class = serializers.UploadProductSerializer
    permission_classes = [IsAuthenticated]


class Search(APIView):
    
    def post(sekf, request):
        data = request.data
        s = SearchSerializer(data=data)
        if s.is_valid():
            o = Product.objects.filter(name__icontains=s.text)
            return Response(ProductSerializer(o, many=True).data)

from rest_framework.pagination import PageNumberPagination
class CommentAPIVeiw(ListAPIView):
    pagination_class = PageNumberPagination
    # queryset = Comment.objects.filter(parent=None)
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        parent_id = self.kwargs.get('pid')
        return Comment.objects.filter(parent=parent_id)
    
    
    # def get(self, request):
    #     c = Comment.objects.filter(parent=None)
    #     s = serializers.CommentSerializer(c, many=True)
    #     return Response(s.data)

# class SellerAPIView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.SellerSerializer