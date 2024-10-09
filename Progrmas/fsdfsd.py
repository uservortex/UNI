def DeterminaPorcentaje(sueldo_base):
    """Determina el porcentaje de aumento según el sueldo base."""
    if sueldo_base > 5000:
        return 10
    elif sueldo_base >= 3501:
        return 15
    elif sueldo_base >= 2001:
        return 20
    else:  # sueldo_base <= 2000
        return 25

def CalculaSueldoTotal(sueldo_base):
    """Calcula el sueldo total a partir del sueldo base y el porcentaje de aumento."""
    porcentaje_aumento = DeterminaPorcentaje(sueldo_base)
    monto_aumento = sueldo_base * (porcentaje_aumento / 100)
    sueldo_total = sueldo_base + monto_aumento
    
    print(f"Sueldo Base: S/. {sueldo_base:.2f}")
    print(f"Monto de Aumento: S/. {monto_aumento:.2f} ({porcentaje_aumento}%)")
    print(f"Sueldo Total: S/. {sueldo_total:.2f}")

# Solicitar al usuario el sueldo base
sueldo_base = float(input("Ingrese el sueldo base del trabajador: S/. "))
CalculaSueldoTotal(sueldo_base)
