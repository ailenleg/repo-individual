# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:19:09 2022

@author: ailen
"""

# Implemente dos funciones (iterativa y recursiva) que devuelvan 
# el resultado de elevar 2 a una potencia entera no negativa. 

print("ingrese un exponente positivo y entero")
n = int(input())

def potencia_iterativa(n): 
    
    potencia = 1
    while n > 0: 
        potencia = potencia*2
        n = n-1
        print(potencia)
    return potencia
    
print(potencia_iterativa(n)) 

print("Potencia recursiva")
def potencia_recursiva(n):
    
    if n == 0: 
        return 1
    potencia = potencia_recursiva(n-1)*2
    print(potencia)
    return potencia #equivalente al potnecia*2


print(potencia_recursiva(n))
    