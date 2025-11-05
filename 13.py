CM_A_YARDAS = 91.44
CM_A_METROS = 100
CM_A_PIES = 30.48
CM_A_PULGADAS = 2.54

valor_cm = float(input("Ingrese un valor en cm: "))

dist_yardas = valor_cm / CM_A_YARDAS
dist_metros = valor_cm / CM_A_METROS
dist_pies = valor_cm / CM_A_PIES
dist_pulgadas = valor_cm / CM_A_PULGADAS

print(valor_cm, "cm equivale a:")
print(dist_yardas, "yardas")
print(dist_metros, "metros")
print(dist_pies, "pies")
print(dist_pulgadas, "pulgadas")
