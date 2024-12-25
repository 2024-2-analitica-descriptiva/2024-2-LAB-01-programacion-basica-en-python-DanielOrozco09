"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():

    import csv
    from collections import Counter

    # Crear un contador para almacenar la cantidad de registros en que aparece cada clave de la columna 5
    key_counter = Counter()

    # Leer el archivo CSV y contar las ocurrencias de cada clave en la columna 5
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            # Obtener los pares clave:valor de la columna 5
            key_value_pairs = row[4].split(',')
            for pair in key_value_pairs:
                key, _ = pair.split(':')
                key_counter[key] += 1

    # Convertir el contador a un diccionario
    key_count_dict = dict(key_counter)

    diccionario_ordenado = {clave: key_count_dict[clave] for clave in sorted(key_count_dict)}

    return diccionario_ordenado

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
