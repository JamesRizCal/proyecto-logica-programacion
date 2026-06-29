"""
Sistema de Gestión de Notas de Estudiantes
Autor: James
 
Descripción:
Este programa permite registrar estudiantes, calcular promedios,
buscar estudiantes y obtener el promedio general del curso.
Se utilizan estructuras condicionales, repetitivas, funciones 
y persistencia de datos mediante archivos JSON.
"""

import json
import os

ARCHIVO_DATOS = "estudiantes.json"

def cargar_datos():
    """Carga los datos del archivo JSON si existe, de lo contrario retorna lista vacía."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_datos():
    """Guarda la lista de estudiantes en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4)

# Lista global donde se almacenan los estudiantes
estudiantes = cargar_datos()

def validar_nota(mensaje):
    """Fuerza al usuario a ingresar una nota numérica entre 0 y 10."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico.")

def agregar_estudiante():
    """Función para registrar un estudiante, validar notas y calcular promedio."""
    nombre = input("\nIngrese el nombre del estudiante: ")

    nota1 = validar_nota("Ingrese nota 1: ")
    nota2 = validar_nota("Ingrese nota 2: ")
    nota3 = validar_nota("Ingrese nota 3: ")

    promedio = round((nota1 + nota2 + nota3) / 3, 2)

    if promedio >= 7:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    estudiantes.append({
        "nombre": nombre,
        "notas": [nota1, nota2, nota3],
        "promedio": promedio,
        "estado": estado
    })
    
    guardar_datos()
    print("\nEstudiante agregado correctamente.\n")

def mostrar_estudiantes():
    """Función para mostrar todos los estudiantes registrados en formato tabla."""
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.\n")
        return

    print("\n" + "-" * 65)
    print(f"{'NOMBRE':<15} | {'N1':<5} | {'N2':<5} | {'N3':<5} | {'PROM':<5} | {'ESTADO':<10}")
    print("-" * 65)

    for est in estudiantes:
        n1, n2, n3 = est.get("notas", [0, 0, 0])
        print(f"{est['nombre']:<15} | {n1:<5} | {n2:<5} | {n3:<5} | {est['promedio']:<5} | {est['estado']:<10}")
    
    print("-" * 65 + "\n")

def buscar_estudiante():
    """Permite buscar un estudiante por nombre de forma exacta."""
    nombre_buscar = input("\nIngrese el nombre a buscar: ")

    for est in estudiantes:
        if est["nombre"].lower() == nombre_buscar.lower():
            print("\nEstudiante encontrado:")
            print(f"Nombre:   {est['nombre']}")
            print(f"Promedio: {est['promedio']}")
            print(f"Estado:   {est['estado']}\n")
            return

    print("\nEstudiante no encontrado.\n")

def promedio_general():
    """Calcula el promedio general del curso."""
    if len(estudiantes) == 0:
        print("\nNo hay datos para calcular promedio.\n")
        return

    suma = sum(est["promedio"] for est in estudiantes)
    promedio = round(suma / len(estudiantes), 2)

    print(f"\nPromedio general del curso: {promedio}\n")

def menu():
    """Menú principal del sistema. Utiliza una estructura repetitiva while."""
    while True:
        print("===== SISTEMA DE NOTAS =====")
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
            print("\nSaliendo del sistema...\n")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.\n")

# Programa principal
if __name__ == "__main__":
    menu()
