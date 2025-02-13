#Encontrar el numero mayor entre 3 numeros dados

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))


if num1 >= num2 and num1 >= num3:
    Num_mayor = num1
else:
    if num2 >= num1 and num2 >= num3:
        Num_mayor = num2
    else:
        Num_mayor = num3

print("El número mayor es:",Num_mayor)