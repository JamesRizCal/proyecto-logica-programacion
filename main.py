"""
Sistema de Gestión de Notas de Estudiantes
Autor: Tu Nombre

Descripción:
Este programa permite registrar estudiantes, calcular promedios,
buscar estudiantes y obtener el promedio general del curso.
Se utilizan estructuras condicionales, repetitivas y funciones.
"""

# Lista global donde se almacenan los estudiantes
estudiantes = []


def agregar_estudiante():
    """
    Función para registrar un estudiante y calcular su promedio.
    """

    nombre = input("Ingrese el nombre del estudiante: ")

    # Validación de notas
    try:
        nota1 = float(input("Ingrese nota 1: "))
        nota2 = float(input("Ingrese nota 2: "))
        nota3 = float(input("Ingrese nota 3: "))
    except:
        print("Error: debe ingresar valores numéricos.")
        return

    # Cálculo del promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Estructura condicional
    if promedio >= 7:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    # Guardar estudiante en la lista
    estudiantes.append({
        "nombre": nombre,
        "promedio": promedio,
        "estado": estado
    })

    print("Estudiante agregado correctamente.\n")


def mostrar_estudiantes():
    """
    Función para mostrar todos los estudiantes registrados.
    """

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.\n")
        return

    for est in estudiantes:
        print("Nombre:", est["nombre"])
        print("Promedio:", round(est["promedio"], 2))
        print("Estado:", est["estado"])
        print("---------------------")


def buscar_estudiante():
    """
    Permite buscar un estudiante por nombre.
    """

    nombre_buscar = input("Ingrese el nombre a buscar: ")

    for est in estudiantes:
        if est["nombre"].lower() == nombre_buscar.lower():
            print("Estudiante encontrado:")
            print(est)
            return

    print("Estudiante no encontrado.\n")


def promedio_general():
    """
    Calcula el promedio general del curso.
    """

    if len(estudiantes) == 0:
        print("No hay datos para calcular promedio.\n")
        return

    suma = 0

    for est in estudiantes:
        suma += est["promedio"]

    promedio = suma / len(estudiantes)

    print("Promedio general del curso:", round(promedio, 2))


def menu():
    """
    Menú principal del sistema.
    Utiliza una estructura repetitiva while.
    """

    while True:

        print("\n===== SISTEMA DE NOTAS =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Promedio general")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            buscar_estudiante()

        elif opcion == "4":
            promedio_general()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


# Programa principal
menu()
