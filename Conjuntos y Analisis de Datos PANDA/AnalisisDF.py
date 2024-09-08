import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox


def primerFila(dataFrame):
    primeros = dataFrame.head()
    return primeros

def ultimaFila(dataFrame):
    ultimas = dataFrame.tail()
    return ultimas

def cantidadElements(dataFrame):
    cantidad = len(dataFrame)
    return cantidad


def cantidadFilasCol(dataFrame):
    cantidad = dataFrame.shape
    return cantidad


def nombreColumnas(dataFrame):
    cantidad = dataFrame.columns.tolist()
    return cantidad


def tipoDatos(dataFrame):
    tipo = dataFrame.dtypes
    return tipo


def resumenDatos(dataFrame):
    resumen = dataFrame.describe()
    return resumen


def agruparPorCantidad(dataFrame, cantidad, nombreCol):
    agrupados = dataFrame[dataFrame[nombreCol] > cantidad]
    return agrupados


def seleccionarColumna(dataFrame, nombreCol):
    if nombreCol in dataFrame.columns:
        columnaX = dataFrame[nombreCol]
        return columnaX
    else:
        return f"Columna {nombreCol} no encontrada."


def seleccionarFilas(dataFrame, fila1, fila2):
    filasX = dataFrame.iloc[fila1:fila2]
    return filasX


def verificarDatosUnicos(dataFrame, nombreCol):
    if nombreCol in dataFrame.columns:
        unicos = dataFrame[nombreCol].value_counts()
        return unicos
    else:
        return f"Columna {nombreCol} no encontrada."


def verificarValoresNulos(dataFrame):
    nulos = dataFrame.isnull().sum()
    return nulos


def eliminarValoresNulos(dataFrame):
    eliminados = dataFrame.dropna()
    return eliminados


def reemplazarValoresNulos(dataFrame, valor):
    dataFrame.fillna(valor, inplace=True)
    return dataFrame


def mostrar_resultado(result):
    messagebox.showinfo("Resultado", str(result))


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
    elif opcion == '6':
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        cantidad = simpledialog.askinteger("Entrada", "Ingrese el valor de cantidad:")
        resultado = agruparPorCantidad(df, cantidad, nombreCol)
    elif opcion == '7':
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        resultado = seleccionarColumna(df, nombreCol)
    elif opcion == '8':
        fila1 = simpledialog.askinteger("Entrada", "Ingrese la primera fila:")
        fila2 = simpledialog.askinteger("Entrada", "Ingrese la segunda fila:")
        resultado = seleccionarFilas(df, fila1, fila2)
    elif opcion == '9':
        nombreCol = simpledialog.askstring("Entrada", "Ingrese el nombre de la columna:")
        resultado = verificarDatosUnicos(df, nombreCol)
    elif opcion == '10':
        resultado = verificarValoresNulos(df)
    elif opcion == '11':
        valor = simpledialog.askstring("Entrada", "Ingrese el valor para reemplazar los nulos:")
        resultado = reemplazarValoresNulos(df, valor)
    elif opcion == '12':
        resultado = eliminarValoresNulos(df)
    elif opcion == '13':
        resultado = ultimaFila(df)
    else:
        resultado = "Opción no válida."

    mostrar_resultado(resultado)


def main():
    np.random.seed(0)

    categorias = ['Presión Arterial', 'Colesterol', 'Glucosa', 'Peso', 'Altura']

    pacientes = [f'Paciente_{i + 1}' for i in range(50)]

    datos = {
        'Presión Sistólica': [
            120, 130, 140, 150, 160, 110, 145, 155, 165, 125,
            135, 145, 155, 165, 175, 185, 195, 125, 135, 145,
            155, 165, 175, 185, 195, 125, 135, 145, 155, 165,
            175, 185, 195, 125, 135, 145, 155, 165, 175, 185,
            195, 125, 135, 145, 155, 165, 175, 185, 195, 125
        ],
        'Presión Diastólica': [
            80, 85, 90, 95, 100, 75, 90, 95, 100, 80,
            85, 90, 95, 100, 105, 110, 115, 80, 85, 90,
            95, 100, 105, 110, 115, 80, 85, 90, 95, 100,
            105, 110, 115, 80, 85, 90, 95, 100, 105, 110,
            115, 80, 85, 90, 95, 100, 105, 110, 115, 80
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
                                        "6: Agrupar por cantidad en 'Peso'\n"
                                        "7: Seleccionar columna\n"
                                        "8: Seleccionar filas\n"
                                        "9: Verificar datos únicos en una columna\n"
                                        "10: Verificar valores nulos\n"
                                        "11: Reemplazar valores nulos\n"
                                        "12: Eliminar valores nulos\n"
                                        "13: Ultimas cinco filas por defecto\n"
                                        "0: Salir"
                                        )

        if opcion == '0':
            break

        ejecutar_opcion(opcion, df)

    root.mainloop()

main()