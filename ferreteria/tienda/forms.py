from django import forms
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False, label='¿Es administrador?')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']
