# -*- coding: utf-8 -*-
import random

simulaciones=100

#Variables

l_rep = [] 			#l_rep es la variable que contiene todos los repuestos que entran al sistema.
na_llegada = []		# Variable que contendrá los números aleatorios para la estimación del tiempo de llegada de los repuestos. 

# Llenado de la variable l_rep con datos correlativos desde 1 hasta el numero ingresado de simulaciones.
for i in range(simulaciones):
	l_rep.append(i)
	na_llegada.append(random.random())

print na_llegada


