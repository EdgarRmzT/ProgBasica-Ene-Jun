#Implementar estructuras de datos basica: pila, cola y lista enlazada


class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        return self.items.pop(0) if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")


print("Ejemplo de Pila:")
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila.desapilar())  

print("\nEjemplo de Cola:")
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.desencolar())  

print("\nEjemplo de Lista Enlazada:")
lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.mostrar()  
