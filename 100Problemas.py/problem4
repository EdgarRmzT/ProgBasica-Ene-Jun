#Secuencia de Fibonacci hasta un numero dado de terminos
numero = int(input("Ingrese el número de términos deseados para la secuancia:"))

def sec(n):                   #Defino secuencia(n), en donde en 'n' es el primer num de termino en la secuencia
    secuencia = [0,1]             #Inicializo la sec con los primeros numeros
    for _ in range(2, n):     #aqui el '_' significa que la variable de iteracion no se usara en el bucle
        secuencia.append(secuencia[-1]+secuencia[-2])    #se obtiene el sig.num de la secuencia sumando los dos 
    return secuencia[:n]                                 #ultimos num de la lista y se añade el valor a la lista usando append()

if numero <=0:
    print("Ingrese un número mayor que 0.")
else:
    print("Secuencia de Fibonacci:", sec(numero))   