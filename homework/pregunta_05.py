"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar el valor máximo y mínimo de la columna 2 por cada letra de la primera columna
    min_max_values = defaultdict(lambda: [float('inf'), float('-inf')])

    # Leer el archivo CSV y encontrar los valores máximos y mínimos de la columna 2 por cada letra en la primera columna
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            letter = row[0]
            value = int(row[1])
            if value < min_max_values[letter][0]:
                min_max_values[letter][0] = value
            if value > min_max_values[letter][1]:
                min_max_values[letter][1] = value

    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    sorted_min_max_values = sorted((letter, values[1], values[0]) for letter, values in min_max_values.items())

    return sorted_min_max_values
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
