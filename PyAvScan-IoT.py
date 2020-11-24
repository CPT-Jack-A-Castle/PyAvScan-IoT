import requests
import hashlib
import numpy as np
import os
import time
import numpy
from timeit import timeit
from os import listdir
from os.path import isfile, isdir

def banner():

    print "__________          _____         _________                                     .___     ___________"
    print "\______   \___.__. /  _  \___  __/   _____/ ____ _____    ____   ____           |   | ___\__    ___/"
    print " |     ___<   |  |/  /_\  \  \/ /\_____  \_/ ___\\\__  \  /    \ /    \   ______ |   |/  _ \|    |   "
    print " |    |    \___  /    |    \   / /        \  \___ / __ \|   |  \   |  \ /_____/ |   (  <_> )    |   "
    print " |____|    / ____\____|__  /\_/ /_______  /\___  >____  /___|  /___|  /         |___|\____/|____|   "
    print "           \/            \/             \/     \/     \/     \/     \/                              "
    time.sleep(1)
    print "** Python Antivirus Scanner IoT - All rights reserved 2020 - Universitat Oberta de Catalunya"
    time.sleep(1)
    print "** Author: Yesith Alexander Alvarez Matta"
    print ""
    time.sleep(1)

url        = "https://virusshare.com/hashes/"


def resumen(ldir, lbas, linfect, timepoTotal):
    print ""
    print "==================================" 
    print "** Python Antivirus Scanner IoT **"
    print "==================================" 
    print "Archivos Analizados: ",ldir
    print "Firmas Consultadas: ",lbas
    print "Archivos Infectados: ",linfect
    print "Tiempo Utilizado: ",timepoTotal,"Segundos"
    print "==================================" 

def listar(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

def leer_Archivo(file):
    with file:
        return file.read()

def eliminar_Archivo(path):
    return os.remove(path)

def hash_Archivo(path):
    return hashlib.md5(leer_Archivo(open( path ,'rb'))).hexdigest()

def contar_archivos(path):
    cantidadArchivos = sum([len(files) for r, d, files in os.walk(path)])
    return cantidadArchivos

def listar_Archivos_Sistema():
    return os.system('sudo find / >> archivosSistema.txt')

def descargar_firmas(url):
    comando = 'sudo wget '
    comando = comando + url
    comando = comando + ' -O firmasdescargadas.txt --recursive'
    print comando
    os.system(comando) 

def obtener_firma():
    inicio = time.time()
    f = open("archivosSistema.txt", "r")
    contador = 0
    archivoInfectados = []
    
    for linea in f:	
	linea = linea.split('\n')
        linea = linea[0]
       	isFile = os.path.isfile(linea)
	if isFile == True:
	   hashMD5 = hash_Archivo(linea)
	   estado = buscar_firma(hashMD5)
	   if estado == 1: 
	      archivo = linea,'=',hashMD5,': Archivo Infectado'
	      print archivo
              archivoInfectados.append(archivo)
	   if estado == 0: 
	      print linea,'=',hashMD5,': Ok'
        contador += 1
 	#print contador
	    
    f.close()
    final = time.time()
    total = round((final - inicio),4)    
    resumen(contador, "1500", archivoInfectados,total)
    return f

def buscar_firma(valor_hash):
    f = open("firmasdescargadas.txt", "r")
    for linea in f:	
	linea = linea.split('\n')
        linea = linea[0]
        if linea == valor_hash:
	   return 1
    f.close()
    return 0

def main():
	try:
		banner()
	        #listar_Archivos_Sistema()
                obtener_firma()
	except:
		banner()
		print("Usage[en]: sudo python PyScan-IoT.py")
		print("Uso[es]:   sudo python PyScan-IoT.py")

if __name__ == '__main__':
     main()






