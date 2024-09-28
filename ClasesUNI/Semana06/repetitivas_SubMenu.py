montoSaldo = 0

while  True:
     print ("\n---MENU PPRINCIPAL---")
     print ("1. Procesar")
     print ("2. Salir")

     while True :
          opcionMenu = int(input("Ingrese una opcion: \t"))

          if (opcionMenu < 1 or opcionMenu > 2) :
               print ("ERROR. Ingresa un menu valido")
          else :
             break
     
     match opcionMenu :
          case 1 :
               while True :
                    print("\n---SUB MENU CAJERO---")
                    print("1. Depositar")
                    print("2. Retirar")
                    print("3. Ver saldo")
                    print("4. Salir")

                    while True :
                         opcionSubMenu = float(input("Ingrese opcion de menu: \t"))

                         if (opcionSubMenu < 1 or opcionSubMenu > 4) :
                              print ("ERROR. Ingrese una opcion valida")
                         else :
                              break
                    
                    match opcionSubMenu:
                         case 1 :
                              while True :
                                   montoDepos = float(input("Ingrese el monto a depositar: \t"))

                                   if (montoDepos <= 0) :
                                        print ("ERROR. Inrese un monto adecaudo: \t")
                                   else :
                                        break
                              montoSaldo = montoSaldo + montoDepos

                         case 2 :
                              while True:
                                   montoRetir = float(input("Ingrese monto a retirar: \t"))
                                   
                                   if (montoRetir <= 0):
                                        print ("ERROR. Ingrese un moto adecaudo a retirar ")

                                   else:
                                        break
                                   
                              if montoRetir <= montoSaldo:
                                   montoSaldo = montoSaldo - montoRetir
                              else :
                                   print ("Saldo insuficiente")

                         case 3:
                              print (f"Su saldo actual es:\t {montoSaldo:.2f}")

                         case 4:
                              while True:
                                   rpta = input("Seguro que quiere volver? (S o s o N o n):\t\t")
                                   rptaMayusc = rpta.upper()
                                   if (rptaMayusc != "S" and rptaMayusc != "N") :
                                        print ("ERROR. Vuelve a ingresar S o s o N o n")
                                   else:
                                        break
                                   
                              if rptaMayusc == "S":
                                   print ("Estas volviendoa al menu principal")
                                   break
            
          case 2:
               while True:
                    rptaMp = input("Seguro que quieres salir? (S o s o N o n):\t\t")
                    rptaMpMayusc = rptaMp.upper()
                    if (rptaMpMayusc != "S" and rptaMpMayusc != "N"):
                         print ("ERROR. Vuelve a ingresar S o s o N o n")
                    else:
                         break
                    
               if rptaMpMayusc == "S":
                    print ("Gracias! Vuelva pronto..")
                    break
                    
               
