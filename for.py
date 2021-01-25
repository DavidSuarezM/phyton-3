# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:28:58 2021

@author: David Suárez Molina
"""

devices=['R1','R2','R3',
         'S1','S2','S3']
listaSW=[]
for x in devices :
    if 'S' in x:
        print(x, end=' ')
    else:
        print('Es router.')
for y in devices:
    if 'S' in y:
        listaSW.append(y)
    else:
        print('\nHola')

print(listaSW)