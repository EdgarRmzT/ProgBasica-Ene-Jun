A= str(input("Ingrese el nombre del archivo:"))

#variable= open(ruta+nombre,modo)

variable= open(A,"w")
B= input(print("Introduzca el nombre del archivo:"), file=variable)
variable.close()


