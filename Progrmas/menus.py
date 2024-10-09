from datetime import datetime
from collections import Counter

# Lista de productos con sus precios
productos = {
    "1": ("Laptop", 1000),
    "2": ("Smartphone", 500),
    "3": ("Tablet", 300),
}

# Carrito de compras, se almacena como lista de tuplas (producto, cantidad, precio unitario)
carrito = []

# Ventas realizadas
ventas_realizadas = []

# Función para obtener el descuento según el día de la semana
def obtener_descuento():
    dia = datetime.now().strftime("%A")  # Obtiene el día de la semana actual
    if dia in ["Thursday", "Friday"]:
        return 0.05  # 5% de descuento
    elif dia in ["Saturday", "Sunday"]:
        return 0.20  # 20% de descuento
    else:
        return 0.0  # Sin descuento

# Función para mostrar el menú principal
def main_menu():
    print("\n========== TIENDA VIRTUAL ==========")
    print("1. Ver productos")
    print("2. Carrito de compras")
    print("3. Finalizar compra")
    print("4. Ver ventas realizadas")
    print("5. Salir")
    print("=====================================")
    option = input("Seleccione una opción: ")
    return option

# Función para mostrar los productos disponibles
def productos_menu():
    print("\n========== PRODUCTOS ==========")
    for key, (nombre, precio) in productos.items():
        print(f"{key}. {nombre} - ${precio}")
    print("4. Regresar al menú principal")
    print("================================")
    option = input("Seleccione un producto para agregar al carrito: ")
    return option

# Función para agregar un producto al carrito
def agregar_al_carrito(opcion):
    if opcion in productos:
        nombre, precio = productos[opcion]
        cantidad = int(input(f"¿Cuántas unidades de {nombre} desea agregar al carrito? "))
        carrito.append((nombre, cantidad, precio))
        print(f"{cantidad} {nombre}(s) agregado(s) al carrito.")
    else:
        print("Opción inválida, intente de nuevo.")

# Función para mostrar el carrito y calcular el total
def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return

    print("\n========== CARRITO ==========")
    total = 0
    contador_productos = Counter()
    
    # Contamos las unidades de cada producto
    for producto, cantidad, precio in carrito:
        contador_productos[producto] += cantidad
    
    # Mostramos los productos en el carrito con sus cantidades
    for producto, cantidad in contador_productos.items():
        precio_unitario = productos[[key for key, value in productos.items() if value[0] == producto][0]][1]
        subtotal = precio_unitario * cantidad
        total += subtotal
        print(f"{producto} ({cantidad}) - Subtotal: ${subtotal:.2f}")

    descuento = obtener_descuento()
    total_con_descuento = total * (1 - descuento)

    print(f"\nTotal antes de descuento: ${total:.2f}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total después de descuento: ${total_con_descuento:.2f}")

# Función para finalizar la compra y registrar la venta
def finalizar_compra():
    if not carrito:
        print("El carrito está vacío. No hay nada para comprar.")
        return

    total = 0
    contador_productos = Counter()

    # Contamos las unidades de cada producto
    for producto, cantidad, precio in carrito:
        contador_productos[producto] += cantidad

    for producto, cantidad in contador_productos.items():
        precio_unitario = productos[[key for key, value in productos.items() if value[0] == producto][0]][1]
        total += precio_unitario * cantidad

    descuento = obtener_descuento()
    total_con_descuento = total * (1 - descuento)

    # Registrar la venta con los productos y cantidades
    ventas_realizadas.append({
        "productos": dict(contador_productos),  # Almacenamos los productos con la cantidad
        "total": total_con_descuento,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print("\nCompra finalizada con éxito.")
    print(f"Total a pagar: ${total_con_descuento:.2f}")
    carrito.clear()  # Vaciamos el carrito después de la compra

# Función para mostrar las ventas realizadas
def ver_ventas_realizadas():
    if not ventas_realizadas:
        print("No se han realizado ventas aún.")
        return

    print("\n========== VENTAS REALIZADAS ==========")
    for i, venta in enumerate(ventas_realizadas, 1):
        print(f"\nVenta {i}:")
        for producto, cantidad in venta["productos"].items():
            print(f"- {producto} ({cantidad})")
        print(f"Total: ${venta['total']:.2f}")
        print(f"Fecha: {venta['fecha']}")
    print("=======================================")

# Función principal que controla el flujo del programa
def main():
    while True:
        option = main_menu()

        if option == "1":
            while True:
                sub_option = productos_menu()

                if sub_option == "4":
                    break  # Regresa al menú principal
                else:
                    agregar_al_carrito(sub_option)

        elif option == "2":
            ver_carrito()

        elif option == "3":
            finalizar_compra()

        elif option == "4":
            ver_ventas_realizadas()

        elif option == "5":
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
        