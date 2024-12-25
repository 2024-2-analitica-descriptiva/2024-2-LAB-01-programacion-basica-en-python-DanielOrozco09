"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
        
    import csv

    # Crear una lista para almacenar las tuplas
    result = []

    # Leer el archivo CSV y contar la cantidad de elementos en las columnas 4 y 5
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            letter = row[0]
            col4_count = len(row[3].split(','))
            col5_count = len(row[4].split(','))
            result.append((letter, col4_count, col5_count))

    return result
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
