# -*- coding: utf-8 -*-
import random
from math import log

# Constantes
simulaciones=10000


#Variables

l_rep = [] 			# l_rep es la variable que contiene todos los repuestos que entran al sistema.
na_llegada = []		# Variable que contendrá los números aleatorios para la estimación del tiempo de llegada de los repuestos. 
te_llegada = []		# tiempo entre llegadas.
h_llegada = []		# hora de llegada.
entrada_mach1 = []	# entrada a la maquina 1
salida_mach1 = [] 	# salida maquina 1
t_bodega1 = []		# tiempo en bodega 1

# Llenado de la variable l_rep con datos correlativos desde 1 hasta el numero ingresado de simulaciones.
# y la variable con los numeros aleatorios para el tiempo entre llegadas de repuestos al sistema.
for i in range(simulaciones):
	l_rep.append(i)
	na_llegada.append(random.random())

# calculo del tiempo entre llegadas.
for i in range(simulaciones):
	t = -0.0588 * log(na_llegada[i])
	te_llegada.append(t)

#Hora de llegada
h_llegada.append(te_llegada[0])
for i in range(1,simulaciones,1):
	h = h_llegada[i-1] + te_llegada[i]
	h_llegada.append(h)

#entrada y salida de la maquina 1 
# Falta algoritmo para considerar cuando la bodega esta llena.
entrada_mach1.append(h_llegada[0])
salida_mach1.append(h_llegada[0]+0.04)
for i in range(1,simulaciones,1):
	if h_llegada[i] > salida_mach1[i-1]:
		entrada_mach1.append(h_llegada[i])
		salida_mach1.append(h_llegada[i]+0.04)
	else:
		entrada_mach1.append(salida_mach1[i-1])
		salida_mach1.append(salida_mach1[i-1]+0.04)

for i in range(simulaciones):
	t_bodega1.append(entrada_mach1[i]-h_llegada[i])

print sum(t_bodega1)/simulaciones


