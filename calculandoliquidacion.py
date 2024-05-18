import os
#VALIDAMOS SI LOS VALORES SON NUMEROS POSITIVOS
def validar_valores(sueldo_base, horas_extra):
    if sueldo_base<=0 or horas_extra<0:
     print("ERROR DATOS MAL INGRESADOS")

#PREGUNTAMOS LOS DATOS DEL TRABAJADOR Y VALIDAMOS SEGUN LAS INSTRUCCIONES
while True:
    nombre_trabajador = input("INGRESA TU NOMBRE: ")
    if len(nombre_trabajador) <= 30:
        sueldo_base = float(input("INGRESA TU SUELDO BASE: "))
        horas_extra = int(input("INGRESA HORAS EXTRAS TRABAJADAS ESTE MES: "))      
        break
    else:
        print("¡EL NOMBRE DEL TRABAJADOR DEBE TENER MAXIMO 30 CARACTERES SIN ESPACIOS! INTENTA NUEVAMENTE")

# CALCULAMOS LA LIQUIDACION
if horas_extra > 180:
    pago_horas_extras = horas_extra * (sueldo_base * 1.5)
else:
    pago_horas_extras = horas_extra * sueldo_base
total_ingresos = sueldo_base + pago_horas_extras
descuento_fonasa = total_ingresos * 0.07
descuento_afp = total_ingresos * 0.10
sueldo_neto = total_ingresos - (descuento_fonasa + descuento_afp)

# MOSTRAMOS LOS DATOS FINALES DE LA LIQUIDACION 
print("\nLIQUIDACION DEL TRABAJADOR:")
print(f"SUELDO BASE: ${sueldo_base:.3f}")
print(f"PAGO POR HORAS EXTRAS: ${pago_horas_extras:.0f}")
print(f"TOTAL INGRESOS: ${total_ingresos:.0f}")
print(f"DESCUENTO  FONASA: ${descuento_fonasa:.0f}")
print(f"DESCUENTO  AFP: ${descuento_afp:.0f}")
print(f"SUELDO NETO A PAGAR: ${sueldo_neto:.3f}")

nombre_archivo = f"Liquidacion_Sueldo_{nombre_trabajador}.txt"

with open(nombre_archivo, 'w') as archivo:
    archivo.write("LIQUIDACION DEL TRABAJADOR:\n")
    archivo.write(f"NOMBRE: {nombre_trabajador}\n")
    archivo.write(f"SUELDO BASE: ${sueldo_base:.3f}\n")
    archivo.write(f"PAGO POR HORAS EXTRAS: ${pago_horas_extras:.0f}\n")
    archivo.write(f"TOTAL INGRESOS: ${total_ingresos:.0f}\n")
    archivo.write(f"DESCUENTO FONASA: ${descuento_fonasa:.0f}\n")
    archivo.write(f"DESCUENTO AFP: ${descuento_afp:.0f}\n")
    archivo.write(f"SUELDO NETO A PAGAR: ${sueldo_neto:.3f}\n")

print("Datos guardados en el archivo:", nombre_archivo)








