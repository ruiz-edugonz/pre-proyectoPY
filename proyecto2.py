productos = []

while True:
    print("\n--- Menú de Productos ---\n\n")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        # Agregar producto
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
        productos.append([nombre, categoria, precio])

    elif opcion == "2":
        # Mostrar productos
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\n--- Lista de Productos ---")
            for i, lista_productos in enumerate(productos, 1):
                print(f"{i}. Nombre: {lista_productos[0].upper()}, Categoría: {lista_productos[1]}, Precio: ${lista_productos[2]}")

    elif opcion == "3":
        # Buscar producto
        termino = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = []
        for lista_productos in productos:
            if termino in lista_productos[0].lower():
                encontrados.append(lista_productos)
        if encontrados:
            print("\nProductos encontrados:")
            for lista_productos in encontrados:
                print(f"Nombre: {lista_productos[0].upper()}, Categoría: {lista_productos[1]}, Precio: ${lista_productos[2]}")
        else:
            print("No se encontraron productos con ese nombre.")

    elif opcion == "4":
        # Eliminar producto
        if not productos:
            print("No hay productos para eliminar.")
        else:
            print("\n--- Lista de Productos ---\n\n")
            for i, lista_productos in enumerate(productos, 1):
                print(f"{i}. Nombre: {lista_productos[0].upper()}, Categoría: {lista_productos[1]}, Precio: ${lista_productos[2]}")
            while True:
                num = input("Ingrese el número del producto a eliminar: ").strip()
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(productos):
                        eliminado = productos.pop(num - 1)
                        print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                        break
                    else:
                        print("Número no se encuentra en la lista.")
                else:
                    print("Ingrese un número válido.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("La opcion no es valida. Intente nuevamente.")