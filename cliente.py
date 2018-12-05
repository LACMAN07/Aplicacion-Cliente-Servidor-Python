#!/usr/bin/env python
# -*- coding: utf-8 -*-
#      client.py

from socket import socket
import subprocess
import datetime

def EnviarArchivo():
    s = socket()
    s.connect(("localhost", 6000))  
    while True:
        archivo = str(raw_input("Nombre del archivo a enviar, seguido del formato (Ej. cosa.mp3)"))
        print(archivo)
        # Con esto obtenemos la hora/fecha
        hora_actual = str(datetime.datetime.now())
        archivoEnviar = open("Archivos/"+archivo, "rb")
        #Aquí voy a crear el archivo .sha256
        sha256 = subprocess.call(('sha256sum Archivos/'+archivo+'>'+'Comprobación/'+archivo+'.sha256'), shell=True)
        # Aqui voy a abrir el archivo que debo crear con la extensión .sha256
        registro= open("Registro/registroCliente.txt", "a")
        registro.write("HORA: "+hora_actual+"   ARCHIVO ENVIADO: "+archivo+"\n")
        registro.write("************************\n")
        content = archivoEnviar.read(1024)
            
        while content:
            s.send(content)
            content = archivoEnviar.read(1024)
        break
        
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
        
    # Cerrar conexión y archivo.
    s.close()
    archivoEnviar.close()
    registro.close()
    print("El archivo ha sido enviado correctamente.")

def EnviandoVerificacion():
    s = socket()
    s.connect(("localhost", 6000))  
    while True:
        archivo = str(raw_input("Ingresa el nombre del archivo que acabas de enviar (Ej. cosa.mp3): "))
        archivoEnviar = open("Comprobación/"+archivo+'.sha256', "rb")
        content = archivoEnviar.read(1024)
            
        while content:
            s.send(content)
            content = archivoEnviar.read(1024)
        break
        
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
        
    # Cerrar conexión y archivo.
    s.close()
    archivoEnviar.close()
    print("El archivo ha sido enviado correctamente.")


def main():
    bandera=1
    while bandera==1:
        EnviarArchivo()
        Comprobacion=raw_input("¿Desea enviar la verificación del archivo? si/no ")
        if Comprobacion=='si' or Comprobacion == 'Si':
            EnviandoVerificacion()
        else:
            print("Es todo por Hoy")   
        continuar = raw_input("¿Quieres enviar otro archivo?: si / no: ")
        if continuar== 'si' or continuar == 'Si':
            bandera = 1
        else: 
            bandera = 0
if __name__ == "__main__":
    main()
