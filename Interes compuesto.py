# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:42:03 2024

@author: USER
"""

capital = float (input ("Ingrese el capital inicial: "))
tasa = float (input ("Ingrese la tasa de interes anual: "))
tiempo = int (input ("Ingrese en tiempo en años: "))

valor_futuro = capital * (1+(tasa/100))**tiempo

print ("El valor futuro del monto inicial es de $" + str(valor_futuro) + " con una tasa de interes del " + str(tasa) + " % durante " + str (tiempo) + " años" )
 