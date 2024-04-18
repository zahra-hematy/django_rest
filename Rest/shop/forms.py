
from .models import *
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ImageForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['id', 'user']
