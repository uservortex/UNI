while True:
    print ('\n===MENU OPCIONES===\n')
    print ('1. Vender')
    print ('2. Salir')

    while True:
        op = int(input('Ingrese una opcion:\t\t'))
        if (op < 1 or op > 2):
            print ('ERROR. Vuelve a ingresar')
        else:
            break

    match op:
        case 1:
            NombreProd = input("Ingrese nombre del producto: \t\t")

            while True:
                PrecioProd = float(input('Ingrese precio de producto:\t\t'))
                
                if (PrecioProd <= 0):
                    print ('ERROR. Vuelve a Ingresar')
                else:
                    break
            
            while True:
                CantidadProd = int(input("Ingrese catidad\t"))

                if (CantidadProd <= 0 ):
                    print ('ERROR. Vuelve a ingresar')
                else:
                    break

            while True:
                PorcentajeDcto = float(input('Ingrese la canntidad de descuento\t'))

                if (PorcentajeDcto <= 0):
                    print ('ERROR. Vuelve a ingresar')
                else:
                    break

            while True:
                Genero = (input('Ingrese su genero\t'))
                GeneroMayus = Genero.upper()

                if (GeneroMayus != 'F' and GeneroMayus != 'M'):
                    print ('ERROR. Veulve a ingresar')
                else:
                    break

            match GeneroMayus:
                case 'F':
                    bono = 0.25
                    if (CantidadProd <= 10 ):
                        dcto = 0.3
                    else:
                        dcto = 0.4

                case 'M':
                    bono = 0.18
                    if (CantidadProd <= 10):
                        dcto = 0.2
                    else:
                        dcto = 0.5
            
            MontoBruto = PrecioProd * CantidadProd
            MontoBono = MontoBruto * bono
            MontoDcto = MontoBruto * PorcentajeDcto
            MontoPago = MontoBruto - MontoDcto + MontoBono

            print ("====REPORTE====")
            print ("El monto bruto:\t", MontoBruto)
            print ("El monto bono:\t",MontoBono)
            print ("El monto descuento:\t", MontoDcto)
            print ("Monto a pagar:\t", MontoPago)

        case 2:
            break

            




