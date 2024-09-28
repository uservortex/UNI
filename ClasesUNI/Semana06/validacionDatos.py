print ("\n===INGRESO DE DATOS===\n")

while True :
    num = eval(input("Ingrese un numero para una vocal: \t\t"))

    if (num < 1 or num > 5) :                  # if (num < 1 or num >5)
        print ("ERROR. Vuelve a ingresar")
    else :
        

        match num :
            case 1 :
                print ("La vocal es a.")
            case 2 :
                print ("La vocal es e.")
            case 3 :
                print ("La vocal es i.")
            case 4 :
                print ("La vocal es o.")
            case 5 :
                print ("La vocal es u.")
        break



# print ("\n===INGRESO DE DATOS===\n")

# while True :
#     num = eval(input("Ingrese un numero para una vocal: \t\t"))

#     if (num < 1 or num > 5) :                  # if (num < 1 or num >5)
#         print ("ERROR. Vuelve a ingresar")
#     else :
#         break 
#     match num :
#         case 1 :
#             print ("La vocal es a.")
#         case 2 :
#             print ("La vocal es e.")
#         case 3 :
#             print ("La vocal es i.")
#         case 4 :
#             print ("La vocal es u.")
#         case 5 :
#             print ("La vocal es u.")



