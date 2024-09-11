from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Vista del logout
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Vista del inicio
def inicio(request):
    return render(request, 'tienda/inicio.html')

# Vista login
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

# Vista register
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

# Vista para listar productos
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/listar_productos.html', {'productos': productos})

# Vista para agregar un producto
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

# Vista para modificar un producto
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
    return render(request, 'tienda/modificar_producto.html', {'form': form})

# Vista para eliminar un producto
@staff_member_required
def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})

# Vista para buscar un producto
@login_required
def buscar_producto(request):
    query = request.GET.get('q', '')  # Obtén el término de búsqueda desde la URL
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)  # Filtra los productos
    else:
        productos = Producto.objects.all()  # Si no hay término de búsqueda, muestra todos los productos
    
    return render(request, 'tienda/buscar_producto.html', {'productos': productos})

# Vista para el perfil del usuario
@login_required
def profile_view(request):
    return render(request, 'tienda/profile.html', {'user': request.user})

# Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'tienda/editar_perfil.html', {'form': form})

# Vista del carrito
from django.shortcuts import redirect, get_object_or_404
from tienda.models import Producto

def agregar_al_carrito(request, id_producto):
    # Obtener el producto a partir del id_producto
    producto = get_object_or_404(Producto, id=id_producto)
    
    # Agregar el producto al carrito (almacenado en la sesión)
    carrito = request.session.get('carrito', [])
    carrito.append({
        'nombre': producto.nombre,
        'precio': producto.precio
    })
    
    # Guardar el carrito de nuevo en la sesión
    request.session['carrito'] = carrito
    
    # Redirigir a la página de productos o carrito
    return redirect('buscar_producto')




def mostrar_carrito(request):
    carrito = request.session.get('carrito', [])
    return render(request, 'tienda/mostrar_carrito.html', {'carrito': carrito})

def eliminar_del_carrito(request, id_producto):
    carrito = request.session.get('carrito', [])
    carrito = [prod for prod in carrito if prod['id_producto'] != id_producto]  # Usamos id_producto
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')


def vaciar_carrito(request):
    request.session['carrito'] = []
    return redirect('mostrar_carrito')



