#Modulo para conversion de Unidades
# programa_principal.py

import conversor 

def main():
    while True:
        print("--- Menú de Conversiones ---")
        print("1. Kilómetros a Millas")
        print("2. Celsius a Fahrenheit")
        print("3. Litros a Galones")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            kilometros = float(input("Ingresa la cantidad de kilómetros: "))
            millas = conversor.kilometros_a_millas(kilometros)
            print(f"{kilometros} kilómetros son {millas} millas.")
        elif opcion == "2":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = conversor.celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
        elif opcion == "3":
            litros = float(input("Ingresa la cantidad de litros: "))
            galones = conversor.litros_a_galones(litros)
            print(f"{litros} litros son {galones} galones.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida, seleccione otra opcion")

if __name__ == "__main__":
    main()
