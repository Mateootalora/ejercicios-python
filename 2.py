import math

lado_a = float(input("Ingrese su primer cateto: "))
lado_b = float(input("Ingrese su segundo cateto: "))

cuadrado_a = lado_a ** 2
cuadrado_b = lado_b ** 2

suma_cuadrados = cuadrado_a + cuadrado_b
hipotenusa_calculada = math.sqrt(suma_cuadrados)

print("La hipotenusa es:", hipotenusa_calculada)
