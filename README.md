# Ferretería Online
# Ferretería Spagnoli

## Descripción
Este proyecto es una tienda online para una ferretería.

## Funcionalidades
1. **Agregar Producto**: Permite añadir nuevos productos al catálogo.
2. **Buscar Producto**: Permite buscar productos por nombre.
3. **Listar Productos**: Muestra todos los productos disponibles en la tienda.
4. **Inicio**: Muestra un home con una nav bar donde tendremos las funcionalidades a utilizar.

## Cómo Ejecutar
1. Clonar el repositorio.
2. Ejecutar migraciones: `python manage.py migrate`.
3. Ejecutar el servidor: `python manage.py runserver`.
4. Acceder a la aplicación en `http://localhost:8000/`.

## Orden de Prueba
1. Agregar un producto en el apartado "Agregar producto".
2. Vizualisarlo dentro del apartado "Listado de productos".
3. Entrar al apartado "Buscar producto" y buscar por su nombre o se puede buscar de forma abreviada por ejemplo = "tarugo" lo buscamos como "tar".
   Igual traeria todos los que tengan en el inico de su nombre "tar", osea si hubiera mas tarugos cargados saldrian todos. 
