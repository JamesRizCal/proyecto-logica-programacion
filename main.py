"""
Sistema de Gestión de Notas de Estudiantes
"""

estudiantes = []


def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")

    nota1 = float(input("Ingrese nota 1: "))
    nota2 = float(input("Ingrese nota 2: "))
    nota3 = float(input("Ingrese nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 7:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    estudiantes.append({
        "nombre": nombre,
        "promedio": promedio,
        "estado": estado
    })

    print("Estudiante agregado")


def mostrar_estudiantes():

    for est in estudiantes:
        print("Nombre:", est["nombre"])
        print("Promedio:", est["promedio"])
        print("Estado:", est["estado"])
        print("----------------")


def menu():

    while True:
        print("\n1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            agregar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            break

        else:
            print("Opción inválida")


menu()
