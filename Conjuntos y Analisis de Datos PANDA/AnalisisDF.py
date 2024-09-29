import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox


def primerFila(dataFrame):
    """
    Returns the first 5 rows of a DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to extract the rows from.
    Returns:
    pandas.DataFrame: The first 5 rows of the DataFrame.
    """
    primeros = dataFrame.head()
    return primeros


def ultimaFila(dataFrame):
    """
    Returns the last 5 rows of a DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to extract the rows from.
    Returns:
    pandas.DataFrame: The last 5 rows of the DataFrame.
    """
    ultimas = dataFrame.tail()
    return ultimas


def unirColumnas(dataFrame, col1, col2, nueva_columna):
    """
    Unites the data from two columns into one and adds it as a new column in the DataFrame,
    displaying unique values vertically.

    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame containing the columns.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    nueva_columna (str): The name of the new column where combined data will be stored.

    Returns:
    pandas.DataFrame: A DataFrame containing only the new column with unique values combined vertically.
    """
    if col1 in dataFrame.columns and col2 in dataFrame.columns:

        dataFrame[nueva_columna] = elementos_unicos(dataFrame,col1).union(elementos_unicos(dataFrame,col2))
        return seleccionarColumna(dataFrame, nueva_columna)
    else:
        return f"Una o ambas columnas '{col1}' y '{col2}' no se encuentran en el DataFrame."

def cantidadElements(dataFrame):
    """
    Returns the number of rows in the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to count the rows from.
    Returns:
    int: The number of rows in the DataFrame.
    """
    cantidad = len(dataFrame)
    return cantidad


def cantidadFilasCol(dataFrame):
    """
    Returns the number of rows and columns in the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to count rows and columns from.
    Returns:
    tuple: A tuple with the number of rows and columns (rows, columns).
    """
    cantidad = dataFrame.shape
    return cantidad


def nombreColumnas(dataFrame):
    """
    Returns the column names of the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to extract column names from.
    Returns:
    list: A list with the column names.
    """
    cantidad = dataFrame.columns.tolist()
    return cantidad


def unirColumnas(dataFrame, col1, col2, nueva_columna):
    """
    Unites the data from two columns into one and adds it as a new column in the DataFrame,
    ensuring unique values.

    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame containing the columns.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    nueva_columna (str): The name of the new column where combined data will be stored.

    Returns:
    pandas.DataFrame: The DataFrame with the new column added.
    """
    # Comprobar si las columnas existen
    if col1 not in dataFrame.columns or col2 not in dataFrame.columns:
        print(f"Una o ambas columnas '{col1}' y '{col2}' no se encuentran en el DataFrame.")
        return dataFrame  # Retorna el DataFrame original si hay error

    # Obtener valores únicos de ambas columnas y eliminar NaN
    unique_values = set(dataFrame[col1].dropna()).union(set(dataFrame[col2].dropna()))

    # Crear la nueva columna con los valores únicos como lista
    dataFrame[nueva_columna] = [list(unique_values)] * len(dataFrame)  # Repite la lista para cada fila

    # Devolver solo el DataFrame con la nueva columna
    return dataFrame[[col1, col2, nueva_columna]]


def tipoDatos(dataFrame):
    """
    Returns the data type of each column in the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to retrieve the data types from.
    Returns:
    pandas.Series: A series containing the data types of each column.
    """
    tipo = dataFrame.dtypes
    return tipo


def agruparPorCantidad(dataFrame, cantidad, nombreCol):
    """
    Filters the DataFrame by values greater than a specified amount in a given column.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to filter.
    cantidad (int): The threshold value for filtering.
    nombreCol (str): The name of the column used for filtering.
    Returns:
    pandas.DataFrame: The filtered DataFrame.
    """
    agrupados = dataFrame[dataFrame[nombreCol] > cantidad]
    return agrupados


def seleccionarColumna(dataFrame, nombreCol):
    """
    Selects a column from the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to select the column from.
    nombreCol (str): The name of the column to select.
    Returns:
    pandas.Series or str: The selected column or an error message if the column is not found.
    """
    if nombreCol in dataFrame.columns:
        columnaX = dataFrame[nombreCol]
        return columnaX
    else:
        return f"Column {nombreCol} not found."


def seleccionarFilas(dataFrame, fila1, fila2):
    """
    Selects a range of rows in the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to select rows from.
    fila1 (int): The starting row (inclusive).
    fila2 (int): The ending row (exclusive).
    Returns:
    pandas.DataFrame: The selected rows from the DataFrame.
    """
    filasX = dataFrame.iloc[fila1:fila2]
    return filasX


def elementos_unicos(dataFrame, nombreCol):
    """
    Finds unique elements in a specific column of the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to search for unique elements.
    nombreCol (str): The name of the column to check for unique values.
    Returns:
    numpy.ndarray or str: Array of unique elements or an error message if the column is not found.
    """
    if nombreCol in dataFrame.columns:
        unicos = dataFrame[nombreCol].unique()
        return unicos
    else:
        return f"Column {nombreCol} not found."


def interseccion_columnas(dataFrame, col1, col2):
    """
    Finds the intersection of two columns.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame containing the columns to intersect.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    Returns:
    numpy.ndarray or str: The intersection of the two columns or an error message if one or both columns are not found.
    """
    if col1 in dataFrame.columns and col2 in dataFrame.columns:
        interseccion = np.intersect1d(dataFrame[col1], dataFrame[col2])
        return interseccion
    else:
        return f"One or both columns {col1}, {col2} not found."


def diferencia_columnas(dataFrame, col1, col2):
    """
    Finds the elements present in col1 but not in col2.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame containing the columns to compare.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    Returns:
    numpy.ndarray or str: The difference between the two columns or an error message if one or both columns are not found.
    """
    if col1 in dataFrame.columns and col2 in dataFrame.columns:
        diferencia = np.setdiff1d(dataFrame[col1], dataFrame[col2])
        return diferencia
    else:
        return f"One or both columns {col1}, {col2} not found."


def verificarValoresNulos(dataFrame):
    """
    Checks for null values in the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to check for null values.
    Returns:
    pandas.Series: A series indicating the number of null values in each column.
    """
    nulos = dataFrame.isnull().sum()
    return nulos


def eliminarValoresNulos(dataFrame):
    """
    Removes rows with null values from the DataFrame.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame from which null values will be removed.
    Returns:
    pandas.DataFrame: A DataFrame with null values removed.
    """
    eliminados = dataFrame.dropna()
    return eliminados


def reemplazarValoresNulos(dataFrame, valor):
    """
    Replaces null values in the DataFrame with a specified value.
    Parameters:
    dataFrame (pandas.DataFrame): The DataFrame to replace null values in.
    valor (any): The value to replace null values with.
    Returns:
    pandas.DataFrame: The DataFrame with null values replaced.
    """
    dataFrame.fillna(valor, inplace=True)
    return dataFrame


def mostrar_resultado(result):
    """
    Displays the result in an information dialog box using tkinter.
    Parameters:
    result (any type): The result to be displayed. It will be converted to a string for display.
    Returns:
    None: Does not return any value, only shows a dialog box.
    """
    messagebox.showinfo("Result", str(result))


def ejecutar_opcion(opcion, df):
    if opcion == '1':
        resultado = primerFila(df)
    elif opcion == '2':
        resultado = cantidadElements(df)
    elif opcion == '3':
        resultado = cantidadFilasCol(df)
    elif opcion == '4':
        resultado = nombreColumnas(df)
    elif opcion == '5':
        resultado = tipoDatos(df)
    elif opcion == '6':  # Nueva opción para unir columnas
        col1 = simpledialog.askstring("Entrada", "Ingrese el nombre de la primera columna a unir:")
        col2 = simpledialog.askstring("Entrada", "Ingrese el nombre de la segunda columna a unir:")
        nueva_columna = simpledialog.askstring("Entrada", "Ingrese el nombre de la nueva columna:")
        resultado = unirColumnas(df, col1, col2, nueva_columna)
    elif opcion == '7':
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        resultado = seleccionarColumna(df, nombreCol)
    elif opcion == '8':
        fila1 = simpledialog.askinteger("Entrada", "Ingrese la primera fila:")
        fila2 = simpledialog.askinteger("Entrada", "Ingrese la segunda fila:")
        resultado = seleccionarFilas(df, fila1, fila2)
    elif opcion == '9':
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        resultado = elementos_unicos(df, nombreCol)
    elif opcion == '10':
        resultado = verificarValoresNulos(df)
    elif opcion == '11':
        valor = simpledialog.askstring("Entrada", "Ingrese el valor para reemplazar los nulos:")
        resultado = reemplazarValoresNulos(df, valor)
    elif opcion == '12':
        resultado = eliminarValoresNulos(df)
    elif opcion == '13':
        resultado = ultimaFila(df)
    elif opcion == '14':  # Elementos únicos en una columna
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        resultado = elementos_unicos(df, nombreCol)
    elif opcion == '15':  # Intersección entre dos columnas
        col1 = simpledialog.askstring("Entrada", "Ingrese el nombre de la primera columna:")
        col2 = simpledialog.askstring("Entrada", "Ingrese el nombre de la segunda columna:")
        resultado = interseccion_columnas(df, col1, col2)
    elif opcion == '16':  # Diferencia entre dos columnas
        col1 = simpledialog.askstring("Entrada", "Ingrese el nombre de la primera columna:")
        col2 = simpledialog.askstring("Entrada", "Ingrese el nombre de la segunda columna:")
        resultado = diferencia_columnas(df, col1, col2)
    else:
        resultado = "Opción no válida."

    mostrar_resultado(resultado)


def main():
    np.random.seed(0)

    categorias = ['sistolica', 'diastolica', 'Colesterol', 'Glucosa', 'Peso', 'Altura']

    pacientes = [f'Paciente_{i + 1}' for i in range(50)]

    datos = {
        'sistolica': [
            120, 130, 140, 150, 160, 110, 145, 155, 165, 125,
            135, 145, 155, 165, 175, 185, 195, 125, 135, 145,
            155, 165, 175, 185, 195, 125, 135, 145, 155, 165,
            175, 185, 195, 125, 135, 145, 155, 165, 175, 185,
            195, 125, 135, 145, 155, 165, 175, 185, 195, 125
        ],
        'diastolica': [
            80, 85, 90, 185, 100, 75, 90, 95, 100, 80,
            85, 90, 95, 100, 105, 110, 115, 80, 85, 90,
            95, 100, 105, 110, 115, 80, 85, 90, 95, 100,
            105, 110, 115, 80, 85, 90, 95, 100, 105, 110,
            115, 80, 85, 90, 95, 100, 105, 120, 115, 80
        ],
        'Colesterol': [
            200, 220, 240, 260, 280, 190, 210, 230, 250, 270,
            200, 220, 240, 260, 280, 190, 210, 230, 250, 270,
            200, 220, 240, 260, 280, 190, 210, 230, 250, 270,
            200, 220, 240, 260, 280, 190, 210, 230, 250, 270,
            200, 220, 240, 260, 280, 190, 210, 230, 250, 270
        ],
        'Glucosa': [
            90, 100, 110, 120, 130, 95, 105, 115, 125, 135,
            90, 100, 110, 120, 130, 95, 105, 115, 125, 135,
            90, 100, 110, 120, 130, 95, 105, 115, 125, 135,
            90, 100, 110, 120, 130, 95, 105, 115, 125, 135,
            90, 100, 110, 120, 130, 95, 105, 115, 125, 135
        ],
        'Peso': [
            60, 70, 80, 90, 100, 65, 75, 85, 95, 105,
            60, 70, 80, 90, 100, 65, 75, 85, 95, 105,
            60, 70, 80, 90, 100, 65, 75, 85, 95, 105,
            60, 70, 80, 90, 100, 65, 75, 85, 95, 105,
            60, 70, 80, 90, 100, 65, 75, 85, 95, 105
        ],
        'Altura': [
            160, 165, 170, 175, 180, 155, 160, 165, 170, 175,
            160, 165, 170, 175, 180, 155, 160, 165, 170, 175,
            160, 165, 170, 175, 180, 155, 160, 165, 170, 175,
            160, 165, 170, 175, 180, 155, 160, 165, 170, 175,
            160, 165, 170, 175, 180, 155, 160, 165, 170, 175
        ]
    }


    df = pd.DataFrame(datos, index=pacientes)

    # OJO ESTA ES LA INTERFAZ GRAFICA
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        opcion = simpledialog.askstring("Entrada",
                                        "Seleccione una opción:\n"
                                        "1: Primeras cinco filas por defecto\n"
                                        "2: Cantidad de elementos\n"
                                        "3: Cantidad de filas y columnas\n"
                                        "4: Nombres de las columnas\n"
                                        "5: Tipos de datos\n"
                                        "6: Unir dos columnas\n"
                                        "7: Seleccionar columna\n"
                                        "8: Seleccionar filas\n"
                                        "9: Verificar datos únicos en una columna\n"
                                        "10: Verificar valores nulos\n"
                                        "11: Reemplazar valores nulos\n"
                                        "12: Eliminar valores nulos\n"
                                        "13: Últimas cinco filas por defecto\n"
                                        "14: Elementos únicos en una columna\n"
                                        "15: Intersección entre dos columnas\n"
                                        "16: Diferencia entre dos columnas\n"
                                        "0: Salir"
                                        )

        if opcion == '0':
            break

        ejecutar_opcion(opcion, df)

    root.mainloop()

main()