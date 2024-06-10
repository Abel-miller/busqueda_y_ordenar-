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

print("Hola, ¿qué quieres hacer?")
opcion = input("1. Ver la calificación más baja\n2. Ver la calificación más alta\nElige una opción (1 o 2): ")


def encontrar_calificacion_mas_baja(estudiantes):
    calif_min = min(estudiantes, key=lambda x: x['calificacion'])
    return calif_min

def encontrar_calificacion_mas_alta(estudiantes):
    calif_max = max(estudiantes, key=lambda x: x['calificacion'])
    return calif_max

if opcion == "1":
    estudiante_calif_baja = encontrar_calificacion_mas_baja(estudiantes)
    print(f"La calificación más baja es de {estudiante_calif_baja['nombre']} en {estudiante_calif_baja['curso']} con {estudiante_calif_baja['calificacion']} puntos.")

elif opcion == "2":
    estudiante_calif_alta = encontrar_calificacion_mas_alta(estudiantes)
    print(f"La calificación más alta es de {estudiante_calif_alta['nombre']} en {estudiante_calif_alta['curso']} con {estudiante_calif_alta['calificacion']} puntos.")

else:
    print("Opción no válida. Por favor, elige 1 o 2.")
