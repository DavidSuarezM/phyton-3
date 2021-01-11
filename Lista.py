# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:37:52 2021

@author: David Suárez Molina
"""

lista=['R1',5,5.8,True,"R1"]
print(lista)
print(type(lista))
print(len(lista)) #Tamaño de la lista
print(lista[2],'\n') #Elemento de la lista
lista[3]=False #Cambiar un valor de la lista
del lista[3] #Borrar un valor de la lista
lista.append('Hola')
print(lista)