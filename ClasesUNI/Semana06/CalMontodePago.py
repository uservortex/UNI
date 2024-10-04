print ("===Ingrese De Datos===\n")
TotalPrecios = 0
for i in range (5):

    while True:
        print ("Ingrese Precio de Producto", i+1 , ":\t\t")
        PrecioPro = float(input())

        if (PrecioPro <= 0):
            print ("Vuelve a ingresar un sdato valido")
        else:
            break

    TotalPrecios = TotalPrecios  + PrecioPro

if TotalPrecios >200:
    dcto = 0.15
else:
    dcto = 0

MontoDcto = TotalPrecios * dcto
MontoPago = TotalPrecios - MontoDcto 

print ('\n===Reporte===\n')
print ('Monto a Pagar: \t\t', TotalPrecios)
print ('Monto Desceunto: \t\t', MontoDcto)
print ('Monto Total a Pagar: \t\t', MontoPago)

