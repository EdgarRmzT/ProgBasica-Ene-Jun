#Calculadora simple de operaciones basicas
a = float(input("Ingrese un numero "))
b = float(input("Ingrese otro numero"))

print("""Seleccione" una opcion
      1-.Suma
      2-.Resta
      3-.Multiplicacion
      4-.Division""")

OP = int(input("ingrese una opcion"))

if OP<1 or OP>4:
    print("Opcion no valida, intente de nuevo")

if OP==1:
    Suma= a+b
    print("La suma de los numeros es =", Suma)

if OP==2:
    Resta= a-b
    print("La resta de los numeros es =", Resta)

if OP==3:
    Multi= a*b
    print("La multiplicacion de los numero es =", Multi)

if OP==4:
    Div= a/b
    print("La division de los numeros es =", Div)


