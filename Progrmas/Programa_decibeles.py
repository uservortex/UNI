
monto_base_dolares = float(input("\nIngresa el monto base en dólares: \t"))
ruido_decibeles = int(input("\nIngresa el ruido en decibeles: \t"))

if ruido_decibeles <= 50:
    categoria = 'A'
    porcentaje_penalidad = 5  
elif ruido_decibeles <= 70:
    categoria = 'B'
    porcentaje_penalidad = 7  
elif ruido_decibeles <= 90:
    categoria = 'C'
    porcentaje_penalidad = 9  
elif ruido_decibeles <= 110:
    categoria = 'D'
    porcentaje_penalidad = 12  
else:
    categoria = 'E'
    porcentaje_penalidad = 15  

# tipo de cambio
tipo_cambio = float(input("\nIngresa el tipo de cambio de dólares a soles: \t"))

# cal. monto base en soles
monto_base_soles = monto_base_dolares * tipo_cambio

# cal. penalidad en soles
penalidad_soles = monto_base_soles * (porcentaje_penalidad / 100)

# cal. monto total a pagar mont base + penalidad
monto_total_pagar = monto_base_soles + penalidad_soles



print("\n+------ Informe Final ------+\n")

print(f"-Categoría asignada: {categoria}")
print(f"-Ruido registrado en decibeles: {ruido_decibeles}")
print(f"-Monto Base en soles: {monto_base_soles:.2f} soles")
print(f"-Penalidad ({porcentaje_penalidad}%): {penalidad_soles:.2f} soles")
print(f"-Monto total a pagar: {monto_total_pagar:.2f} soles")
