"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
        
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar la suma de la columna 2 para cada letra de la columna 4
    letter_sums = defaultdict(int)

    # Leer el archivo CSV y sumar los valores de la columna 2 para cada letra en la columna 4
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            value = int(row[1])
            letters = row[3].split(',')
            for letter in letters:
                letter_sums[letter] += value

    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente por clave
    sorted_letter_sums = dict(sorted(letter_sums.items()))

    return sorted_letter_sums

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
