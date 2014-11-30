# -*- coding: utf-8 -*-
import random
from math import log

# Constantes
simulaciones=100


#Variables

l_rep = [] 			# l_rep es la variable que contiene todos los repuestos que entran al sistema.
na_llegada = []		# Variable que contendrá los números aleatorios para la estimación del tiempo de llegada de los repuestos. 
te_llegada = []		# tiempo entre llegadas.

# Llenado de la variable l_rep con datos correlativos desde 1 hasta el numero ingresado de simulaciones.
# y la variable con los numeros aleatorios para el tiempo entre llegadas de repuestos al sistema.
for i in range(simulaciones):
	l_rep.append(i)
	na_llegada.append(random.random())

# calculo del tiempo entre llegadas.
for i in range(simulaciones):
	t = -0.0588 * log(na_llegada[i])
	te_llegada.append(t)

print te_llegada
