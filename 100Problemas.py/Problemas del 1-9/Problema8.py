#Calcular area y la circunferencia de un circulo
radio= float(input("Ingrese el radio del circulo:"))

if radio<=0:
    print("Ingrese otro valor")
else:
    Circunferencia= 2*3.14*radio
    Area= 3.14*(radio**2)
    print("El area del circulo es:", Area)
    print("La circunferencia del circulo es de:", Circunferencia)