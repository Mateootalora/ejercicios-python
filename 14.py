capital_inicial = float(input("Cuanto fue el dinero invertido: "))
tasa_interes = float(input("cuanto seria tu porcentaje de interes: "))
periodo_dias = float(input("cuanto es el periodo al que estas dispuesto a esperar: "))

interes_bruto = (capital_inicial * (tasa_interes / 100) * periodo_dias) / 360

TASA_RETENCION = 0.07
valor_retencion = interes_bruto * TASA_RETENCION

valor_a_recibir = capital_inicial + interes_bruto - valor_retencion

print("El valor de su interes bruto es de:", interes_bruto)
print("Con el descuento del 7% (retención), el valor descontado es de:", valor_retencion)
print("El valor final a recibir es de:", valor_a_recibir)
