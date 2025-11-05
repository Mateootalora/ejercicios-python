var_uno = input("Ingrese el valor para la variable A: ")
var_dos = input("Ingrese el valor para la variable B: ")

temporal = var_uno
var_uno = var_dos
var_dos = temporal

print("El nuevo valor de A es:", var_uno)
print("El nuevo valor de B es:", var_dos)


