#Generar lista de numeros pares e impares hasta un limite dado
Limite= int(input("Ingresa un limite:"))

if Limite<=0:
    print("ingrese otro valor")
    
par=[]  #estos dos son lo mismo 
impar = list()

for num in range(1,Limite+1):          #secuencia de numeros del 1 hasta el limite
    if num % 2 == 0:         #este comprueba si es par 
        par.append(num)
    else:                    #se almacenan en las listas, dependiendo si son par o impar
        impar.append(num)

impresion = max(len(par),len(impar))          #devuelve un valor maximo entre a y b o de las dos listas, par o impar
#el len(lista) o 'len' desenvuelven la cantidad de elementos dentro de las listas, devuelven el numero de elementos en las listas de numeros

for item in range(impresion):
    try:                                   #el try intenta ejecutar un bloque de codigo
        print(par[item], impar[item])
    except IndexError:                 #el except maneja los errores, el index error hace que si una lista no tiene elementos, se asigna un '-'
        try:
            v1=par[item]
        except IndexError:
            v1='-'
        try:
            v2=impar[item]
        except:
            v2='-'
        finally:
            print(v1, v2)