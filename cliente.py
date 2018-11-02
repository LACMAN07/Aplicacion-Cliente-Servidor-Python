#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#
#      client.py
#
#
from socket import socket
def main():
    s = socket()
    s.connect(("localhost", 6000))
        
    while True:
        archivo = str(input("Nombre del archivo a enviar, seguido del formato (Ej. cosa.mp3)"))
        archivoEnviar = open(archivo, "rb")
        content = archivoEnviar.read(1024)
            
        while content:
            # Enviar contenido.
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
if __name__ == "__main__":
    main()
