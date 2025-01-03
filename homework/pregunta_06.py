"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    
    import csv
    from collections import defaultdict

    # Crear un diccionario para almacenar el valor máximo y mínimo por cada clave en la columna 5
    min_max_dict = defaultdict(lambda: [float('inf'), float('-inf')])

    # Leer el archivo CSV y procesar los valores de la columna 5
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            # Obtener los pares clave:valor de la columna 5
            key_value_pairs = row[4].split(',')
            for pair in key_value_pairs:
                key, value = pair.split(':')
                value = int(value)
                if value < min_max_dict[key][0]:
                    min_max_dict[key][0] = value
                if value > min_max_dict[key][1]:
                    min_max_dict[key][1] = value

    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente por clave
    sorted_min_max_dict = sorted((key, values[0], values[1]) for key, values in min_max_dict.items())

    return sorted_min_max_dict

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
