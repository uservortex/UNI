contadorPedidCompleto  = 0
contadorPedidIncompleto = 0
contadorPedidos = 0

while True:
    print ("===MENU PRINCIPAL===")
    print ("1. Ingresar stock inicial")
    print ("2. Salir")

    while True:
        opMenu = int(input("Ingrese una opcion"))
        if (opMenu < 1 or opMenu > 2):
            print ("ERROR. Vuelve a ingresar")
        else:
            break

    match opMenu:
        case 1:
            while True:
                cantidadStock = int(input("Ingrese stock para vender:\t"))
                if (cantidadStock <= 0):
                    print ("ERROR. Vuelve a ingresar")
                else:
                    break

            while True:
                print ("===SUB MENU: VENTAS===")
                print ("1. Ventas")
                print ("2. Reportar")
                print ("3. Volver")

                while True:
                    opSubMenu = int(input("Ingrese una opcion"))
                    if (opSubMenu < 1 or opSubMenu > 3 ):
                        print ("ERROR. Ingrese una opcion valida")
                    else:
                        break
                
                match opSubMenu:
                    case 1:
                        while True:
                            cantidadPedida = int(input("Ingrese cantidad pedida a vender:\t"))
                            if (cantidadPedida <= 0):
                                print ("ERROR. Vuelva a ingresar")
                            else:
                                break
                        contadorPedidos += 1        #CANTIDAD DE CLIENTE

                        if cantidadPedida <= cantidadStock:
                            cantidadStock -= cantidadPedida
                            contadorPedidCompleto += 1
                            print ("===PEDIDO COMPLETO===")
                        else:
                            contadorPedidIncompleto += 1
                            print ("===PEDIDO INCOMPLETO===")

                            falta = cantidadPedida - cantidadStock
                            print ("---Falta completar:", falta)

                    case 2:
                        print ("\n===REPORTE TOTAL===\n")
                        print ("La cantidad total de clientes que pidieron:\t\t", contadorPedidos)
                        print ("La cantidad de pedidos completos:\t\t", contadorPedidCompleto)
                        print ("La cantidad de pedidos imcompletos:\t\t", contadorPedidIncompleto)
                        print ("Lo que queda en el stock:\t\t", cantidadStock)

                    case 3:
                        print ("Vuelve al menu principal..!")
                        break

        case 2:
            while True:
                rptaMp = input("Seguro que quieres salir? (S o s o N o n):\t\t")
                rptaMpMayus = rptaMp.upper()
                if(rptaMpMayus != "S" and rptaMpMayus != "N"):
                    print ("ERROR. Vuelve a ingresar S o s o N o n")
                else:
                    break
            if rptaMpMayus == "S":
                print ("Gracais.. Vuelva pronto..!")
                break








# Elaborar un programa para una empresa que tiene un stock inicial, y debe ingresar la cantidad pedida. 
# Reportar: 
# La cantidad total de clientes atendidos (solo si se completó todo el pedido)
# La cantidad total de clientes no atendidos (no se completó pedido).
# El stock de unidades que queda del producto.
# El total acumulado vendido del producto.
# Usar Menú de Opciones (con la opción Salir) y Validar cada dato ingresado