estudiantes = [
    {"nombre": "Juan", "curso": "Matemáticas", "calificacion": 85},
    {"nombre": "María", "curso": "Ciencias", "calificacion": 92},
    {"nombre": "Ana", "curso": "Física", "calificacion": 65},
    {"nombre": "Luis", "curso": "Química", "calificacion": 70},
    {"nombre": "Marta", "curso": "Informática", "calificacion": 82},
    {"nombre": "Raúl", "curso": "Geografía", "calificacion": 73},
    {"nombre": "Sofía", "curso": "Programación", "calificacion": 90},
    {"nombre": "Julia", "curso": "Arquitectura", "calificacion": 84},
    {"nombre": "Fernando", "curso": "Dibujo", "calificacion": 95},
    {"nombre": "Lucía", "curso": "Música", "calificacion": 68},
]

def ordenar_estudiantes(estudiantes, clave):
    for i in range(len(estudiantes) - 1):
        min_idx = i
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[j][clave] < estudiantes[min_idx][clave]:
                min_idx = j
        estudiantes[i], estudiantes[min_idx] = estudiantes[min_idx], estudiantes[i]

print("Hola, ¿qué quieres hacer?")
opcion = input("1. Ordenar por nombre\n2. Ordenar por calificación\nElige 1 o 2: ")

if opcion == '1':
    ordenar_estudiantes(estudiantes, "nombre")
    print("Ordenado por nombre:")
elif opcion == '2':
    ordenar_estudiantes(estudiantes, "calificacion")
    print("Ordenado por calificación:")
else:
    print("Opción no válida")

for estudiante in estudiantes:
    print(estudiante)
