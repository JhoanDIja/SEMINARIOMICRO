#!/usr/bin/env python3
"""
    secuenvia-listo.py
    Presenta una secuencia que se puede usar 
    para indicar que un sistema esta listo
    para ser utilizado
"""

import time
import os

"""
Una función que abre un archivo cualquiera para leer, lee el contenido y cierra el archivo,
devuelve su contenido.
"""
def LeerArchivo(archivo):
    try:
        textfile= open(archivo,'r')
        print(textfile.read(),flush=True)
        return textfile
    except:
        print("Este archivo no existe")

# LeerArchivo("/home/albertdipre/Desktop/SEMINARIOMICRO/PRUEBASPY/miarchsivo.txt")

"""
Una función para escribir un texto que le pasen como argumento, en un archivo cualquiera, y
devuelve lo que escribió.
"""
def EscribirArchivo(ArchivoEscrito,texto):
    try:
        textfile=open(ArchivoEscrito,"x")
        textfile.write(texto)
        return textfile
    except:
        print("No se puede escribir en este archivo o intentaste poner un archivo ya existente")
    
# EscribirArchivo("/home/albertdipre/Desktop/SEMINARIOMICRO/PRUEBASPY/miarchsivo.txt")


"""
Una función que lea el contenido de 4 archivos de nombre secuencial (“a0, a1, a2, a3”), que
solo contienen una palabra, guarde el contenido de cada uno y lo sobrescriba con otra
palabra; devuelve una tupla con el contenido de cada archivo. Acepta como argumentos un
path base1 y el contenido a escribir.
"""

def leer_escribir_archivos(path_base, contenido_a_escribir):
    resultados = []
    
    for i in range(4):
        # Construir el nombre del archivo secuencial
        nombre_archivo = path_base + str(i)
        
        # Leer el contenido del archivo actual
        with open(nombre_archivo, 'r') as archivo:
            contenido_actual = archivo.read().strip()
            resultados.append(contenido_actual)
        
        # Sobrescribir el contenido del archivo con la nueva palabra
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido_a_escribir)
    
    return tuple(resultados)

# Ejemplo de uso

"""
Una función que le escriba una palabra a cuatro archivos de nombre “bN”, 𝑁 ∈ [0,3], en
secuencia, esperando un tiempo entre cada escritura. El archivo imprime cada vez que hace
una escritura, pero el comando print solo imprime una nueva línea cuando termina la
secuencia2
. Acepta como argumentos el path base, y el tiempo entre escrituras
"""

def escribir_con_espera(path_base, palabra, tiempo_entre_escrituras):
    for i in range(4):
        # Construir el nombre del archivo secuencial
        nombre_archivo = path_base + "b" + str(i)
        
        # Escribir la palabra en el archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(palabra)
        
        # Imprimir que se ha realizado la escritura
        print(f"Escritura en {nombre_archivo}", flush=True)
        
        # Esperar el tiempo especificado entre escrituras
        time.sleep(tiempo_entre_escrituras)


path_base_a = "C:/Users/alber/OneDrive/Escritorio/SEM/SEMINARIOMICRO/Dipre/a"
path_base_b= "C:/Users/alber/OneDrive/Escritorio/SEM/SEMINARIOMICRO/Dipre/b"
contenido_a_escribir = "desactivado"
palabras_secuencia_1 = "Hola Mundo"
palabras_secuencia_2 = "Adios Mundo"
tiempo_entre_escrituras = 1


# Guardando los contenido aN
contenido_original_a = leer_escribir_archivos(path_base_a, contenido_a_escribir)

leer_escribir_archivos(path_base_a,contenido_a_escribir)

#Guardando los contenidos bN
escribir_con_espera(path_base_b, palabras_secuencia_1, tiempo_entre_escrituras)

escribir_con_espera(path_base_b, palabras_secuencia_2, tiempo_entre_escrituras)

# Restaurar el contenido original en los archivos "aN"
leer_escribir_archivos(path_base_a, contenido_original_a)

