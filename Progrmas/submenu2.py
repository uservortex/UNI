from collections import Counter

# Diccionario con productos y submenús con diferentes precios
productos = {
    "articulos": {
        "nombre": "Artículos",
        "variantes": {
            1: ("Bolígrafo", 1),
            2: ("Cuaderno", 3),
            3: ("Agenda", 5),
            4: ("Mochila", 20)
        }
    },
    "informatica": {
        "nombre": "Informática",
        "variantes": {
            1: ("Teclado", 15),
            2: ("Mouse", 10),
            3: ("Monitor", 120),
            4: ("Impresora", 150)
        }
    },
    "electronica": {
        "nombre": "Electrónica",
        "variantes": {
            1: ("Auriculares", 50),
            2: ("Cámara", 300),
            3: ("Tablet", 200),
            4: ("Smartphone", 500)
        }
    }
}

# Carrito de compras (lista de tuplas)
carrito = []
ventas_realizadas = Counter()

# Días en los que hay descuentos (conjunto)
dias_con_descuento_5 = {"jueves", "viernes"}
dias_con_descuento_8 = {"sábado", "domingo"}

# Función para mostrar el submenú de categorías
def mostrar_categorias():
    print("\n--- Categorías Disponibles ---")
    print("1. Artículos")
    print("2. Informática")
    print("3. Electrónica")
    opcion = int(input("Seleccione una categoría: "))
    if opcion == 1:
        return "articulos"
    elif opcion == 2:
        return "informatica"
    elif opcion == 3:
        return "electronica"
    else:
        print("Opción inválida, intente de nuevo.")
        return None

# Función para mostrar submenús de productos dentro de una categoría
def mostrar_submenu(categoria):
    if categoria in productos:
        print(f"\n--- Opciones de {productos[categoria]['nombre']} ---")
        for key, (nombre, precio) in productos[categoria]["variantes"].items():
            print(f"{key}. {nombre} - ${precio}")
        sub_opcion = int(input("Seleccione el producto que desea agregar: "))
        return sub_opcion
    else:
        print("Categoría inválida.")
        return None

# Función para agregar productos al carrito
def agregar_al_carrito(categoria):
    sub_opcion = mostrar_submenu(categoria)
    if sub_opcion and sub_opcion in productos[categoria]["variantes"]:
        nombre, precio = productos[categoria]["variantes"][sub_opcion]
        cantidad = int(input(f"¿Cuántas unidades de {nombre} desea agregar? "))
        carrito.append((nombre, cantidad, precio))  # Tupla: (producto, cantidad, precio)
        ventas_realizadas[nombre] += cantidad
        print(f"{cantidad} {nombre}(s) agregado(s) al carrito.")
    else:
        print("Opción inválida.")

# Función para mostrar los productos en el carrito
def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("\n--- Artículos en el carrito ---")
        for nombre, cantidad, precio in carrito:
            print(f"{nombre} - {cantidad} unidades - ${precio} c/u")

# Función para aplicar descuento según el día de la semana
def aplicar_descuento(total, dia_semana):
    if dia_semana in dias_con_descuento_5:
        descuento = 0.05
    elif dia_semana in dias_con_descuento_8:
        descuento = 0.08
    else:
        descuento = 0

    total_descuento = total * descuento
    total_final = total - total_descuento
    print(f"Se ha aplicado un descuento de {descuento * 100}%: -${total_descuento:.2f}")
    return total_final

# Función para finalizar la compra
def finalizar_compra():
    if not carrito:
        print("No hay productos en el carrito para comprar.")
        return

    total = sum(cantidad * precio for _, cantidad, precio in carrito)
    dia_semana = input("Ingrese el día de la semana: ").lower()
    total_con_descuento = aplicar_descuento(total, dia_semana)
    
    print(f"\nTotal a pagar: ${total_con_descuento:.2f}")
    carrito.clear()  # Vaciar el carrito después de la compra

# Función para mostrar ventas realizadas
def mostrar_ventas_realizadas():
    if not ventas_realizadas:
        print("No se han registrado ventas aún.")
    else:
        print("\n--- Ventas realizadas ---")
        for producto, cantidad in ventas_realizadas.items():
            print(f"{producto}: {cantidad} unidades vendidas")

# Función principal del menú
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver productos")
        print("2. Ver carrito")
        print("3. Finalizar compra")
        print("4. Ver ventas realizadas")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            categoria = mostrar_categorias()
            if categoria:
                agregar_al_carrito(categoria)
        elif opcion == 2:
            mostrar_carrito()
        elif opcion == 3:
            finalizar_compra()
        elif opcion == 4:
            mostrar_ventas_realizadas()
        elif opcion == 5:
            print("Gracias por su compra. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el programa
menu_principal()
