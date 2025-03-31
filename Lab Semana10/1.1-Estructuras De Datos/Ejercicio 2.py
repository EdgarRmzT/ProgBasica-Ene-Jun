#Manejo de inventario con listas y Diccionarios

# Inicializar el inventario como una lista de diccionarios
inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))

    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")

    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
            return

    print(f"Producto '{nombre}' no encontrado en el inventario.")

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")

    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            return

    print(f"Producto '{nombre}' no encontrado en el inventario.")

def mostrar_productos():
    inventario_ordenado = sorted(inventario, key=lambda x: x["precio"])

    print("Productos en el inventario (ordenados por precio):")
    for producto in inventario_ordenado:
        print(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

# Menú principal
while True:
    print("--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        mostrar_productos()
    elif opcion == "5":
        break
    else:
        print("Opción no válida, seleccionaotra opcion.")
