"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
        
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar la suma de los valores de la columna 5 para cada letra de la columna 1
    letter_sums = defaultdict(int)

    # Leer el archivo CSV y sumar los valores de la columna 5 para cada letra en la columna 1
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            letter = row[0]
            key_value_pairs = row[4].split(',')
            for pair in key_value_pairs:
                _, value = pair.split(':')
                letter_sums[letter] += int(value)

    # Convertir el diccionario a un diccionario ordenado alfabéticamente por clave
    sorted_letter_sums = dict(sorted(letter_sums.items()))

    return sorted_letter_sums
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
