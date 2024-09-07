from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required




#Vista del logout
def logout_view(request):
    logout(request)
    return redirect('inicio')

#Vista del inicio
def inicio(request):
    return render(request, 'tienda/inicio.html')

#Vista login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'tienda/login.html', {'form': form})

#Vista register
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tienda/register.html', {'form': form})

# Vista para modificar un producto
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/listar_productos.html', {'productos': productos})

@login_required
@staff_member_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto.html', {'form': form})

@login_required
@staff_member_required
def modificar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/modificar_producto.html', {'form': form, 'producto': producto})

@login_required
@staff_member_required
def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})

#Vista para busacr un producto
def buscar_producto(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'tienda/buscar_producto.html', {'productos': productos})


@staff_member_required
def agregar_producto(request):
    # Lógica para agregar productos
    pass

@staff_member_required
def modificar_producto(request, producto_id):
    # Lógica para modificar productos
    pass

@staff_member_required
def eliminar_producto(request, producto_id):
    # Lógica para eliminar productos
    pass

@login_required
def profile_view(request):
    return render(request, 'tienda/profile.html', {'user': request.user})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'tienda/editar_perfil.html', {'form': form})