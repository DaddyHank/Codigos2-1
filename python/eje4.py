# Calcular el promedio de calificaciones de estudiantes
def calcular_promedio(calificaciones):
    suma = 0
    for estudiante, notas in calificaciones.items():
        suma += sum(notas)
    promedio = suma / len(calificaciones)
    return promedio

def calcular_promedio(notas):
    return sum(notas) / len(notas)

calificaciones = {'Estudiante1': [8.5, 9.0, 7.8],
                  'Estudiante2': [9.2, 8.8, 9.5],
                  'Estudiante3': [7.8, 8.2, 8.0]}

for estudiante, notas in calificaciones.items():
    promedio_estudiante = calcular_promedio(notas)
    print(f'El promedio de calificaciones es: {promedio_estudiante}')

#el error se encontraba en el +1 de la línea 6 y hacía falta una función para calcular el promedio por separado de
#cada estudiante
