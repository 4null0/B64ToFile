#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import argparse

miParser = argparse.ArgumentParser ()

miParser.add_argument('-o', '--origen', metavar="FICHERO ORIGEN", help="Fichero con contiene la cadena en base64", required=True, type=str)
miParser.add_argument('-d', '--destino', metavar="FICHERO DESTINO", help="Fichero donde se almacenarán los datos decodificados", required=True, type=str)

args = miParser.parse_args()

#Abrimos el fichero que contiene la información en base64
fichero = open(args.origen,"r")

#Leemos el contenido del archivo, lo decodificamos y los dejamos en una variable
cadenabase64 = fichero.read()
contenido = base64.b64decode(cadenabase64)

#Hay que cerrar las cosas
fichero.close()

#Abrimos el fichero donde dejaremos la cadena de información decodificada
fichero2 = open(args.destino,"wb")

#Salvamos la información decodificada
fichero2.write(contenido)

#No olvides cerrar, porque si no la información no se transfiere al disco duro
fichero2.close()
