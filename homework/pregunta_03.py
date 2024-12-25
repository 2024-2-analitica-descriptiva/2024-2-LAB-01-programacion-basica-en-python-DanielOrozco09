"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar la suma de la columna 2 por cada letra de la primera columna
    sums = defaultdict(int)

    # Leer el archivo CSV y sumar los valores de la columna 2 por cada letra en la primera columna
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            letter = row[0]
            value = int(row[1])
            sums[letter] += value

    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    sorted_sums = sorted(sums.items())

    return sorted_sums

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
