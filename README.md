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
1. Loguearte o registrarte, asi su usuario se crea dentro de la Base de datos o se buscar y se le permite el
   ingreso con sus debidos permisos. 
2. Si es un usuario normal solo podra buscar productos con el buscador y no realizar otro tipo de acciones.
3. Si es un usuario admin o con permisos, podra agregar/editar/eliminar productos a su parecer, al igual que un usuario normal
   podra utlizar el buscador y ver los nuevos productos creados.
