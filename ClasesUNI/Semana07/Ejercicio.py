
contMasc = 0
contFem = 0
contTotalClien = 0
cantMascMayMil = 0
acumTotalVentas = 0 
acumVentasFem = 0

while True:
    print ("===MENU OPCIONES===")
    print ("1. Procesar")
    print ("2. Reportar")
    print ("3. Salir")

    while True:
        op = int(input("Ingrese una opcion\t"))
        if (op < 1 or op >3):
            print ("ERROR. Ingrese unaopcion correcta")
        else:
            break
    
    match op:
        case 1:
            nombreProd = input("Ingrese nombre de producto\t ")

            while True:
                precioProd = float(input("Ingrese precio del producto:\t\t"))
                if (precioProd <= 0 ):
                    print ("ERROR. Vuelve a ingresar")
                else:
                    break
            
            while True:
                cantProd = int(input("Ingrese cantida de producto\t"))
                if (cantProd <= 0):
                    print ("ERROR. Vuelve a ingresar")
                else:
                    break
            
            while True:
                cantDcto = float(input("Ingrese porcentaje de descuento:\t"))
                if ( cantDcto <= 0):
                    print ("ERROR. Vuelve a Ingresar")
                else:
                    break

            while True:
                Genero = (input("Ingrese su genero:\t"))
                GeneroMayus = Genero.upper()
                
                if (GeneroMayus != "F" and GeneroMayus != "M"):
                    print ("ERROR. Vuelve a ingresar")
                else:
                    break

            match GeneroMayus:
                case "F":
                    contFem = contFem + 1

                    bono = 0.25
                    if (cantProd <= 10):
                        dcto = 0.3
                    else:
                        dcto = 0.4

                case "M":
                    contMasc = contMasc + 1 

                    bono = 0.18
                    if(cantProd <= 10):
                        dcto = 0.2
                    else:
                        dcto = 0.5

            MontoBruto = precioProd * cantProd
            MontoBono = MontoBruto * bono
            MontoDcto = MontoBruto * cantDcto
            MontoPago = MontoBruto - MontoDcto + MontoBono

            contTotalClien = contTotalClien + 1 
            acumTotalVentas = acumTotalVentas + MontoPago

            if (GeneroMayus == "F"):
                acumVentasFem = acumVentasFem + MontoPago

            if (GeneroMayus == "M" and acumTotalVentas >= 1000):
                cantMascMayMil = cantMascMayMil + 1 

            print ("\n===REPORTE===\n")
            print ("El monto bruto es:\t\t", MontoBruto)
            print ("El monto bono es:\t\t", MontoBono)
            print ("El monto descuento es:\t\t", MontoDcto)
            print ("El monto a pagar es:\t\t", MontoPago)
        
        case 2:
            print ("\n===REPORTE POR TOTAL===\n")
            print ("La cantidad total de clientes es:\t", contTotalClien)
            print ("La cantidad de clientes femeninos es:\t", contFem)
            print ("La cantida de clientes masculinos es:\t", contMasc)
            print ("La cantida de clientes masculino, acumulado >= 1000 es:\t", cantMascMayMil)
            print ("El  acumulado total de venta es:\t", acumTotalVentas)
            print ("El acumulado total de ventas de cliente femenino es:\t", acumVentasFem)
        
        case 3:
            print ("Gracias por su visita")
            break
                    



# PROGRAMA CON OPCIONES, CONTADORES Y ACUMULADORES

# Se require calcular el monto total de pago, luego de ingresar el 
# genero del cliente, ademas de la cantidad de productos a adquirir, 
# con su respectivo precio. Para calcular le monto total a pagar, se
# asignan descuentos segun el genero y la cantidada adquirida. Tambien
# moatrar la cantidad de clientes, la cantidad de clientes de genero
# masculino, la cantidad de clientes de genero femenino, la cantidad de 
# clientes de genero masculino que tiene acumulado de ventas >= 1000, 
# el acumulado en total de las ventas , el acumulado de las ventas de 
# clientes de genero femenino.