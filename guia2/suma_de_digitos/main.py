# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:30:03 2022

@author: ailen
"""


def sumadedigitos(n): 
    
    if n == 0:
        return 0
    return sumadedigitos(n//10) + n%10

print(sumadedigitos(250))


    