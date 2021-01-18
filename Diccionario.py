# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:14:16 2021

@author: David Suárez Molina
"""

ipAddress={"R1":"10.1.1.1", 1:'AP', 2:2.5, 3:True}
print(type (ipAddress))
print(len (ipAddress))
print(ipAddress)
print(ipAddress[2]) #Para mostrar valores específicos.
ipAddress['R3']='10.0.0.3'
print('R3' in ipAddress)
