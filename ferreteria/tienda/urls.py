from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('modificar/<int:id_producto>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/editar/', views.editar_perfil, name='editar_perfil'),

    path('carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('agregar-al-carrito/<int:id_producto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:id_producto>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]

