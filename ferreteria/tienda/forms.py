from django import forms
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False, label='¿Es administrador?')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Podrías personalizar el formulario según el contexto (ej. permisos)
        if not self.current_user.is_superuser:
            self.fields['is_staff'].widget = forms.HiddenInput()  # Ocultar para usuarios no superusuario

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_staff']:
            user.is_staff = True  # Marcar como administrador si corresponde
        if commit:
            user.save()
        return user

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en stock'}),
        }
