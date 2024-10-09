from collections import Counter

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre} - ${self.precio}"

class Carrito:
    def __init__(self):
        self.items = []
        self.ventas_realizadas = Counter()

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))
        self.ventas_realizadas[producto.nombre] += cantidad

    def mostrar_carrito(self):
        if not self.items:
            print("El carrito está vacío.")
        else:
            print("\n--- Artículos en el carrito ---")
            for producto, cantidad in self.items:
                print(f"{producto.nombre} - {cantidad} unidades - ${producto.precio} c/u")

    def total(self):
        return sum(cantidad * producto.precio for producto, cantidad in self.items)

    def vaciar(self):
        self.items.clear()

class Tienda:
    def __init__(self):
        self.productos = {
            "articulos": {
                "nombre": "Artículos",
                "variantes": {
                    1: Producto("Bolígrafo", 1),
                    2: Producto("Cuaderno", 3),
                    3: Producto("Agenda", 5),
                    4: Producto("Mochila", 20)
                }
            },
            "informatica": {
                "nombre": "Informática",
                "variantes": {
                    1: Producto("Teclado", 15),
                    2: Producto("Mouse", 10),
                    3: Producto("Monitor", 120),
                    4: Producto("Impresora", 150)
                }
            },
            "electronica": {
                "nombre": "Electrónica",
                "variantes": {
                    1: Producto("Auriculares", 50),
                    2: Producto("Cámara", 300),
                    3: Producto("Tablet", 200),
                    4: Producto("Smartphone", 500)
                }
            }
        }
        self.carrito = Carrito()
        self.dias_con_descuento_5 = {"jueves", "viernes"}
        self.dias_con_descuento_8 = {"sábado", "domingo"}

    def mostrar_categorias(self):
        print("\n--- Categorías Disponibles ---")
        print("1. Artículos")
        print("2. Informática")
        print("3. Electrónica")
        opcion = input("Seleccione una categoría: ")
        return self.seleccionar_categoria(opcion)

    def seleccionar_categoria(self, opcion):
        categorias = {
            "1": "articulos",
            "2": "informatica",
            "3": "electronica"
        }
        return categorias.get(opcion)

    def mostrar_submenu(self, categoria):
        if categoria in self.productos:
            print(f"\n--- Opciones de {self.productos[categoria]['nombre']} ---")
            for key, producto in self.productos[categoria]["variantes"].items():
                print(f"{key}. {producto}")
            sub_opcion = input("Seleccione el producto que desea agregar: ")
            return self.agregar_al_carrito(categoria, sub_opcion)
        else:
            print("Categoría inválida.")

    def agregar_al_carrito(self, categoria, sub_opcion):
        if sub_opcion.isdigit() and int(sub_opcion) in self.productos[categoria]["variantes"]:
            producto = self.productos[categoria]["variantes"][int(sub_opcion)]
            cantidad = int(input(f"¿Cuántas unidades de {producto.nombre} desea agregar? "))
            self.carrito.agregar_producto(producto, cantidad)
            print(f"{cantidad} {producto.nombre}(s) agregado(s) al carrito.")
        else:
            print("Opción inválida.")

    def aplicar_descuento(self, total, dia_semana):
        descuento = 0
        if dia_semana in self.dias_con_descuento_5:
            descuento = 0.05
        elif dia_semana in self.dias_con_descuento_8:
            descuento = 0.08

        total_descuento = total * descuento
        total_final = total - total_descuento
        print(f"Se ha aplicado un descuento de {descuento * 100}%: -${total_descuento:.2f}")
        return total_final

    def finalizar_compra(self):
        if not self.carrito.items:
            print("No hay productos en el carrito para comprar.")
            return

        total = self.carrito.total()
        dia_semana = input("Ingrese el día de la semana: ").lower()
        total_con_descuento = self.aplicar_descuento(total, dia_semana)
        
        print(f"\nTotal a pagar: ${total_con_descuento:.2f}")
        self.carrito.vaciar()  # Vaciar el carrito después de la compra

    def mostrar_ventas_realizadas(self):
        if not self.carrito.ventas_realizadas:
            print("No se han registrado ventas aún.")
        else:
            print("\n--- Ventas realizadas ---")
            for producto, cantidad in self.carrito.ventas_realizadas.items():
                print(f"{producto}: {cantidad} unidades vendidas")

def menu_principal():
    tienda = Tienda()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver productos")
        print("2. Ver carrito")
        print("3. Finalizar compra")
        print("4. Ver ventas realizadas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            categoria = tienda.mostrar_categorias()
            if categoria:
                tienda.mostrar_submenu(categoria)
        elif opcion == "2":
            tienda.carrito.mostrar_carrito()
        elif opcion == "3":
            tienda.finalizar_compra()
        elif opcion == "4":
            tienda.mostrar_ventas_realizadas()
        elif opcion == "5":
            print("Gracias por su compra. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el programa
menu_principal()
