import math
a = float(input('Introduce el termino cuadratico: '))
b = float(input('Introduce el termino lineal: '))
c = float(input('Introduce el termino independiente: '))

def f_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        x1 = complex(parte_real, parte_imaginaria)
        x2 = complex(parte_real, -parte_imaginaria)
        return "Dos soluciones complejas son: x1 =", (x1), "x2 =", (x2)
    elif discriminante == 0:
        x = -b / (2*a)
        return "Una solución: x =",(x)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return "Dos soluciones: x1 =",(x1), "x2 =",(x2)
    
print(f_cuadratica(a,b,c))