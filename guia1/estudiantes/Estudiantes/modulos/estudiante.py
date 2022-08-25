# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:32:25 2022

@author: alumno
"""
class Estudiante :
    
    def __init__(self, p_legajo, p_ap, p_nom, p_dni, p_promedio):
        self.legajo = p_legajo
        self.apellido = p_ap
        self.nombre = p_nom
        self.dni = p_dni
        self.promedio = p_promedio
        
    @property
    def legajo(self):
        return self._legajo
    
    @legajo.setter
    def legajo(self, valor): 
        self._legajo = valor 
    
    @property
    def apellido(self):
        return self._apellido
    
    
    @apellido.setter
    def apellido(self, valor): 
        self._apellido = valor

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor): 
        self._nombre = valor
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor): 
        self._dni = valor 
        
    @property
    def promedio(self):
        return self._promedio
    
    @promedio.setter
    def promedio(self, valor): 
        self._promedio = valor 
        
    def __lt__(self, otro):
        return self.legajo < otro.legajo
    