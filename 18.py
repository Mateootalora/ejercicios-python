import math

radio_base = float(input("Ingrese su radio: "))
altura_cilindro = float(input("Ingrese su altura: "))

area_base = math.pi * (radio_base ** 2)
volumen_total = area_base * altura_cilindro

print("El volumen del cilindro es:", volumen_total)


