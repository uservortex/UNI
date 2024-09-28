
montoSaldo = 0

while True:
    print ("\n---MENU CAJERO---\n")
    print ("1. Depositar")
    print ("2. Retirar")
    print ("3. Ver saldo")
    print ("4. Salir")

    while   True:
        OpcionMenu = int(input("Ingrese opcion del menu: \t\t"))

        if (OpcionMenu < 1 or OpcionMenu > 4):
            print ("ERROR. Vuelve a ingresar una opcion")
        
        else :
            break

    match OpcionMenu :
        case 1 :
            while True :
                MontoDepos = float (input("Ingrese Monto a Depositar: \t"))

                if (MontoDepos <= 0) :
                    print ("ERROR. Vuelva a ingresar un monto mayor a 0")

                else :
                    break
            montoSaldo = montoSaldo + MontoDepos
        
        case 2 :
            while True :
                montoRetir = float(input("Ingrese el monto a retirar \t"))

                if (montoRetir <= 0):
                    print ("ERROR. El monto debe ser mayor a 0")
                else :
                    break
            montoSaldo = montoSaldo - montoRetir

        case 3 :
            print ("Su saldo actual es: \t", montoSaldo )

        case 4 :
            print ("Gracias! Vuelva pronto..")

            break



            # FALTA AGREGAR DETALLES

        

