#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      server.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#
from socket import socket, error
def main():
    s = socket()
        
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6000))
    s.listen(0)
        
    conn, addr = s.accept()
    nombre = str(raw_input("nombre de archivo a guardar: "))
    archivoEnviar = open(nombre, "wb")
    contador = 1    
    while archivoEnviar == archivoEnviar:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
            print("Estoy en el try")
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
                    print("Segundo If")
                if not end:
                    # Almacenar datos.
                    archivoEnviar.write(input_data)
                    print("Primer Ifnot")
                else:
                    break
        contador = contador+1
        
    print("El archivo se ha recibido correctamente.")
    archivoEnviar.close()
if __name__ == "__main__":
    main()