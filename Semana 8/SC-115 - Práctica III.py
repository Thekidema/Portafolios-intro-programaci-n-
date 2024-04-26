def mostrar_productos(grupo, productos):
    print(f"Productos en el grupo {grupo}:")
    for i, producto in enumerate(productos, 1):
        print(f"Producto {i}: {producto}")
    print()
def agregar_producto(grupo, productos):
    producto = input(f" Agregar producto al grupo  '{grupo}': ")
    if producto in productos:
        print("El producto ya no tiene existecia.")
    else:
        productos.append(producto)
        print(f"Producto '{producto}' agregado al grupo '{grupo}'.")
        mostrar_productos(grupo, productos)
def eliminar_producto(grupo, productos):
    producto = input(f"Ingrese el nombre del producto que desea eliminar del grupo '{grupo}': ")
    if producto in productos:
        productos.remove(producto)
        print(f"Producto '{producto}' eliminado del grupo '{grupo}'.")
        mostrar_productos(grupo, productos)
    else:
        print("El producto no existe en este grupo.")
def actualizar_producto(grupo, productos):
    producto_antiguo = input(f"Ingrese el nombre del producto que desea actualizar en el grupo '{grupo}': ")
    if producto_antiguo in productos:
        producto_nuevo = input(f"Ingrese el nuevo nombre para '{producto_antiguo}': ")
        index = productos.index(producto_antiguo)
        productos[index] = producto_nuevo
        print(f"Producto '{producto_antiguo}' actualizado a '{producto_nuevo}' en el grupo '{grupo}'.")
        mostrar_productos(grupo, productos)
    else:
        print("El producto ya no existe en este grupo.")

articulos_enlatados = ["Sardinas", "Atún", "Frijoles"]
productos_limpieza = ["Suavitel", "Jabón en polvo", "Limpiador de ventanas"] #USO DEL PROGRAMA
carnes = ["Pescado", "Carne molida", "Chorizo"]
granos = ["Arroz", "garbanzos", "Lentejas,"]

agregar_producto("Articulos enlatados", articulos_enlatados)
agregar_producto("Productos de limpieza", productos_limpieza)
agregar_producto("Carnes", carnes)
agregar_producto("Granos", granos)

eliminar_producto("Articulos enlatados", articulos_enlatados)  #DE ESTA MANERA SE ELIMINAN LOS PRODUCTOS 

actualizar_producto("Carnes", carnes)   #LA OPCION DE  PODER ACTULIZAR EL PRODUCTO

agregar_producto("Granos", granos)    # AGREGAR UN PRODUCTO YA EXISTENETE 

mostrar_productos("Articulos enlatados", articulos_enlatados)
mostrar_productos("Productos de limpieza", productos_limpieza)   # CON ESTA BARRA DE CODIGO SE MOSTRARAN LOS PRODUCTOS FINALES 
mostrar_productos("Carnes", carnes)
mostrar_productos("Granos", granos)
