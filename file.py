# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:46:16 2021

@author: David Suárez Molina
"""

file=open('devices.txt','r')
for item in file:
    print(item)

file.close()
