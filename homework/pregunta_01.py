"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():

    import csv

    # Inicializar la suma
    suma_columna_2 = 0

    # Leer el archivo CSV y sumar los valores de la columna 2
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            suma_columna_2 += int(row[1])

    return suma_columna_2


"""
Retorne la suma de la segunda columna.

Rta/
214

"""
