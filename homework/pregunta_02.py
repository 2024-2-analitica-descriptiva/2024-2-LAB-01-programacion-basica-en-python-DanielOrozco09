"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    
    import csv
    from collections import Counter

    # Leer el archivo CSV y contar las ocurrencias de cada letra en la primera columna
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        first_column = [row[0] for row in reader]

    # Contar las ocurrencias de cada letra
    counter = Counter(first_column)

    # Convertir el contador a una lista de tuplas y ordenarla alfabéticamente
    sorted_counts = sorted(counter.items())

    return sorted_counts

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
