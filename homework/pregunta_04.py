"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    
    import csv
    from collections import Counter

    # Crear un contador para almacenar la cantidad de registros por cada mes
    month_counter = Counter()

    # Leer el archivo CSV y contar los registros por cada mes en la columna 3
    with open('./files/input/data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            date = row[2]
            month = date[5:7]  # Extraer el mes de la fecha en formato YYYY-MM-DD
            month_counter[month] += 1

    # Convertir el contador a una lista de tuplas y ordenarla por mes
    sorted_month_counts = sorted(month_counter.items())

    return sorted_month_counts

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
