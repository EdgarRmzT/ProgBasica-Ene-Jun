#Implementacion de multiples paradigmas

# Paradigma Imperativo
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print("Suma (Imperativo):", suma)

# Paradigma Estructurado
def calcular_suma(lista):
    total = 0
    for num in lista:
        total += num
    return total

print("Suma (Paradigma estructurado):", calcular_suma(numeros))

# Paradigma Modular
def sumatoria(a,b):
    return a+b

print("Suma (paradigma modular):", sumatoria(5,6))


# Paradigma Orientado a Objetos
class Calculadora:
    def __init__(self, lista):
        self.lista = lista
    
    def calcular_suma(self):
        return sum(self.lista)

calc = Calculadora(numeros)
print("Suma (Paradigma OO):", calc.calcular_suma())