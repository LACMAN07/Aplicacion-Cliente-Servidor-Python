#!/usr/bin/env python
# -*- coding: utf-8 -*-
#      server.py
from socket import socket, error
import subprocess
import datetime

def recibirArchivo():
    s = socket()   
    s.bind(("localhost", 6000))
    s.listen(5)
    conn, addr = s.accept()
    nombre = str(raw_input("nombre de archivo a guardar: "))
    archivoEnviar = open("Archivos/"+nombre, "wb")
    hora_actual = str(datetime.datetime.now())
    registro= open("Registro/registroServidor.txt", "a")
    registro.write("HORA: "+hora_actual+"   ARCHIVO RECIBIDO: "+nombre+"\n")
    registro.write("************************\n")
    while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
            if not len(input_data):
                break
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1

                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    archivoEnviar.write(input_data)
                else:
                    break
    print("El archivo se ha recibido correctamente.")
    archivoEnviar.close()
def verificacion():
    s = socket()   
    s.bind(("localhost", 6000))
    s.listen(5)
    conn, addr = s.accept()
    nombre = str(raw_input("nombre de archivo que guardó: "))

    archivoEnviar = open("Archivos/"+nombre+'.sha256', "wb")
    while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
            if not len(input_data):
                break
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1

                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    archivoEnviar.write(input_data)
                else:
                    break
    archivoEnviar.close()
    print("Se ha recibido el archivo de Comprobacion")
def main():
    bandera = 1
    while bandera == 1: 
        recibirArchivo()
        Comprobacion=raw_input("¿Desea recibir la verificación del archivo? si/no ")
        if Comprobacion=='si' or Comprobacion == 'Si':
            verificacion()
        else:
            print("Es todo por Hoy")   
        continuar = raw_input("¿Quieres recibir otro archivo?: si / no: ")
        if continuar== 'si' or continuar == 'Si':
            bandera = 1
        else: 
            bandera = 0
if __name__ == "__main__":
    main() 
