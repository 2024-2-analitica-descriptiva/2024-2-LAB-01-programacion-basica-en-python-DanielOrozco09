"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    value_to_letters = defaultdict(set)

    # Leer el archivo CSV y asociar las letras a los valores de la columna 2
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            value = int(row[1])
            letter = row[0]
            value_to_letters[value].add(letter)

    # Convertir el diccionario a una lista de tuplas, ordenar las letras y ordenar por los valores de la columna 2
    sorted_value_to_letters = sorted((value, sorted(letters)) for value, letters in value_to_letters.items())

    return sorted_value_to_letters

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
