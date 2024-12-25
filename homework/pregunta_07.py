"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    value_to_letters = defaultdict(list)

    # Leer el archivo CSV y asociar las letras a los valores de la columna 2
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            value = int(row[1])
            letter = row[0]
            value_to_letters[value].append(letter)

    # Convertir el diccionario a una lista de tuplas y ordenarla por los valores de la columna 2
    sorted_value_to_letters = sorted(value_to_letters.items())

    return sorted_value_to_letters
    
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
