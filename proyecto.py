# pre-proyecto/proyecto.py

def mostrar_menu():
    print("\n\n--- Menú de Productos ---\n")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def ingresar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")
    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        print("La categoría no puede estar vacía.")
    while True:
        precio = input("Ingrese el precio del producto (sin centavos): ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        print("El precio debe ser un número entero positivo.")
    return [nombre, categoria, precio]

def mostrar_productos(productos): # Función para mostrar los productos que se ingresaron
    if not productos:
        print("No hay productos registrados.")
        return
    print("\n--- Lista de Productos ---\n")
    for i, lista_producto in enumerate(productos, 1):
        print(f"{i}. Nombre: {lista_producto[0].upper()},\n Categoría: {lista_producto[1]},\n Precio: ${lista_producto[2]}")

def buscar_producto(productos):  # Función para buscar los productos que se ingreso
    termino = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrados = [lista_producto for lista_producto in productos if termino in lista_producto[0].lower()]
    if encontrados:
        print("\nProductos encontrados:")
        for lista_producto in encontrados:
            print(f"Nombre: {lista_producto[0].upper()}, Categoría: {lista_producto[1]}, Precio: ${lista_producto[2]}")
    else:
        print("No se encontraron productos con ese nombre.")

def eliminar_producto(productos):
    if not productos:
        print("No hay productos para eliminar.")
        return
    mostrar_productos(productos)
    while True:
        opcion = input("Ingrese el número del producto a eliminar: ").strip()
        if opcion.isdigit():  # Verifica si la entrada es un número
            i = int(opcion)
            if 1 <= i <= len(productos):
                eliminado = productos.pop(i - 1)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                break
            else:
                print("Número no encontrado en la lista.")
        else:
            print("Ingrese un número válido.")

def menu():
    productos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            productos.append(ingresar_producto())
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no es válida. Intente nuevamente.")


menu()


