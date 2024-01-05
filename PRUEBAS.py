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

# LeerArchivo("/home/albertdipre/Desktop/SEMINARIOMICRO/PRUEBASPY/miarchsivo.txt")

"""
Una función para escribir un texto que le pasen como argumento, en un archivo cualquiera, y
devuelve lo que escribió.
"""


