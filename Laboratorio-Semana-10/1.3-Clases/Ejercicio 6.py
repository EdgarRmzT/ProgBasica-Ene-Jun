#Sistema de gestion de vehiculos

class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo}, Año: {self.año}, Precio: ${self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, puertas):
        super().__init__(marca, modelo, año, precio)
        self.puertas = puertas

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

# Ingreso de datos del usuario
tipo = input("Ingrese el tipo de vehículo (auto/moto): ")
marca = input("Marca: ")
modelo = input("Modelo: ")
año = int(input("Año: "))
precio = float(input("Precio: "))

if tipo.lower() == "auto":
    puertas = int(input("Número de puertas: "))
    vehiculo = Automovil(marca, modelo, año, precio, puertas)
elif tipo.lower() == "moto":
    cilindrada = int(input("Cilindrada (cc): "))
    vehiculo = Motocicleta(marca, modelo, año, precio, cilindrada)
else:
    print("Tipo de vehículo no válido.")
    exit()

print(vehiculo.mostrar_info())