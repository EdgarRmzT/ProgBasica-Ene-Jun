#Calculadora de numeros factoriales
A = int(input("Introduzca un numero factorial:"))

if A<0:
    print("No se puede calcular el factorial de un numero negativo")
else:
    if A==0 or A==1:
        Resultado=1
        print("El factorial de", A, "es:", Resultado)
    else:
        Resultado=1
        for i in range(2,A+1): #Esto calcula el factorial multiplicando todos los numeros de 2 hasta el numero que en este caso es A
            Resultado= Resultado*i
        print("El factorial de", A, "es:", Resultado)


