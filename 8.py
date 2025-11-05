PORCENTAJE_SALUD = 0.04
PORCENTAJE_PENSION = 0.04

salario_bruto = float(input("Vamos a determinar tus descuentos de salud y pension. Ingresa tu salario base: "))
print("Tu salario base es de:", salario_bruto)

descuento_salud = salario_bruto * PORCENTAJE_SALUD
descuento_pension = salario_bruto * PORCENTAJE_PENSION
aporte_total = descuento_salud + descuento_pension

print("El valor del aporte total (salud + pension) es de:", aporte_total)
print("El valor del descuento de salud es de:", descuento_salud)
print("El valor del descuento de pension es de:", descuento_pension)
