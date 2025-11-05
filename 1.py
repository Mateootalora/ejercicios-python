import math

entrada_numerica = float(input("Ingrese su numero: "))

val_seno = math.sin(entrada_numerica)
val_coseno = math.cos(entrada_numerica)
val_tangente = math.tan(entrada_numerica)

val_raiz = None
if entrada_numerica >= 0:
    val_raiz = math.sqrt(entrada_numerica)
    
val_log = None
if entrada_numerica > 0:
    val_log = math.log(entrada_numerica)

print("Resultados para el numero:", entrada_numerica)
print("El seno es:", val_seno)
print("El coseno es:", val_coseno)
print("La tangente es:", val_tangente)
print("La raiz cuadrada es:", val_raiz)
print("El logaritmo natural es:", val_log)
