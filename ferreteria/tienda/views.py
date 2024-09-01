from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

#Vista del inicio
def inicio(request):
    return render(request, 'tienda/inicio.html')

# Vista para modificar un producto
def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/modificar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/listar_productos.html', {'productos': productos})

#Vista oara agregar un producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()

    return render(request, 'tienda/agregar_producto.html', {'form': form})

#Vista para busacr un producto
def buscar_producto(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'tienda/buscar_producto.html', {'productos': productos})