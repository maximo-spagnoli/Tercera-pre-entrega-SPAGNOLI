from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Nueva vista para la página de inicio
    path('productos/', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('modificar/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
