contadorCurso = 0                   #CONTADOR
acumuladorCredito = 0               #ACUMULADOR

while True:
    print ("===MENU OPCIONES===")
    print ("1. Procesar")
    print ("2. Reportar")
    print ("3. Salir")

    while True:
        op = int(input("Ingrese una opcion\t"))
        if (op < 1 or op > 3):
            print ("ERROR> Vuelve a ingresar")
        else:
            break

    match op:
        case 1:
            nombreCurso = input("Ingrese el nombre del curso: \t")
            contadorCurso = contadorCurso + 1 

            while True:
                creditoCurso = int(input("Ingrese creditos (1 al 5) de curso:\t\t"))
                if (creditoCurso <= 0 or creditoCurso >= 6):
                    print ("ERROR. Ingresa de nuevo")
                else:
                    break
            acumuladorCredito = acumuladorCredito + creditoCurso

        case 2:
            print ("\n===REPORTE POR TOTAL===\n")
            print ("Total cantidad de cursos \t\t", contadorCurso )
            print ("El acumulado de creditos es:\t", acumuladorCredito)

        case 3:
            print ("Gracias, Vuelva pronto..!")
            break



# Elaborar un programa para un alumno, ingresar el nombre
# del curso y su respectiva cantidad de créditos (de 1 a 5) y
# mostrar la cantidad de cursos ingresados y el acumulado de créditos.
# Usar Menú de opciones y validar datos

    


