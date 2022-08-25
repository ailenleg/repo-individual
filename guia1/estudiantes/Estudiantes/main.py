# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:30:26 2022

@author: alumno
"""

# En un archivo de texto están guardados los datos de los estudiantes de una escuela. 
# Cada línea posee los datos de un estudiante separados por comas. 
# Leer el archivo, agregar cada registro en un objeto de tipo Estudiante, almacenarlos en una lista 
# y mostrar los datos ordenados por legajo

# with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/alumnos.txt") as archivo:
#     contenido = archivo.readlines()
#     print(contenido)
#     archivo.close()

from modulos.estudiante import Estudiante 
    
archivo = open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/alumnos.txt")
contenido = archivo.read();
print(contenido)
archivo.close()

# with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/alumnos.txt") as archivo:
#     for linea in archivo:
#         print (linea, end="")

with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/alumnos.txt") as archivo:
    l_archivo = list(archivo)
    print (l_archivo)

# ESCRIBIR ARCHIVOS
# with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/archivonuevo.txt", mode='w') as archivo:
#     n = archivo.write("Archivo nuevo .\nArchivo. n\hola angie")
#     print(n)
    
# with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/archivonuevo.txt", mode='a') as archivo:
#     n = archivo.write("Archivo nuevo .\nArchivo. :D")
#     print(n)
    
# with open("C:/Users/alumno/Desktop/algoritmosailen/estudiantes/Estudiantes/archivonuevo.txt", mode='r+') as archivo:
#     n = archivo.write("Archivo nuevo .\nArchivo. allala")
#     print(n)

print("------------------A---------------------")

with open("../estudiantes/alumnos.txt") as archivo:
    for nro_lineas, linea in enumerate(archivo):
        print(f" {nro_lineas}: {linea.strip()}")
print("-------------------B--------------------")


lista_estudiantes = []

for linea in l_archivo: 
    lista_datos = linea.split(",")
    print(lista_datos)        
    d_estudiante = Estudiante(int(lista_datos[0]),lista_datos[1],lista_datos[2],lista_datos[3],lista_datos[4])
    lista_estudiantes.append(d_estudiante)
print("------------C------------")
print(lista_estudiantes)
    


#cadena.slip() -> separa cadena x espacios, si agrego caracter lo separa c eso 
print("------------D------------")
print("----Lista ordenada por legajo----")

lista_ordenanda = sorted(lista_estudiantes)
print(lista_ordenanda)

for i in lista_ordenanda:
    print(i.legajo)

