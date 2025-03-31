#Gestion de contactos con tuplas y estructuras aninadadas

agenda = []

def agregar_contacto():
    print("--- Agregar nuevo contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    nuevo_contacto = (nombre, telefono, correo)
    agenda.append(nuevo_contacto)
    print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto():
    print("--- Buscar contacto ---")
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    encontrado = False
    
    for contacto in agenda:
       if contacto[0].lower() == nombre_buscar.lower():
            print("Detalles del contacto:")
            print(f"Nombre: {contacto[0]}")
            print(f"Teléfono: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Contacto no encontrado.")

def listar_contactos():
    print("--- Lista de contactos (orden alfabético) ---")
    if not agenda:
        print("La agenda está vacía.")
        return
    
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}")
        print(f"Teléfono: {contacto[1]}")
        print(f"Correo: {contacto[2]}")

while True:
    print("--- AGENDA DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar todos los contactos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        listar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Elija otra opcion")