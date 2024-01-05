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
        print(textfile.read())
        return textfile
    except:
        print("Este archivo no existe")

LeerArchivo("/home/albertdipre/Desktop/SEMINARIOMICRO/PRUEBASPY/miarchsivo.txt")

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
    
EscribirArchivo("/home/albertdipre/Desktop/SEMINARIOMICRO/PRUEBASPY/miarchsivo.txt")


def CambiarPalabra(a):
    for i in range(0,3):
        try:
            textfile =open(a,"x")
        except:
            print("Error")



