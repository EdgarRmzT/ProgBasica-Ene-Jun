#Modificar, editar y leer un archivo de texto

import os

def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    else:
        print("El archivo no existe.")

def modificar_archivo(nombre_archivo, texto_nuevo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write('\n' + texto_nuevo)
    else:
        print("El archivo no existe.")

nombre = str(input("introduzca el nombre del archivo:"))
escribir_archivo(nombre, str(input("Introduzca lo que quiera escribir en el archivo de texto:")))
print("Contenido del archivo:")
print(leer_archivo(nombre))

modificar_archivo(nombre, "Este es un nuevo contenido agregado.")
print("Contenido después de la modificación:")
print(leer_archivo(nombre))
