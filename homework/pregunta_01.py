"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():

    column_names = ['Letra', 'Numero', 'Fecha', 'Serie','Codigo']
    data = pd.read_csv("../files/input/data.csv",
        sep="	",
        names = column_names
        # thousands=None,
        # decimal=".",
    )

    suma = data['Numero'].sum()

    return suma
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
