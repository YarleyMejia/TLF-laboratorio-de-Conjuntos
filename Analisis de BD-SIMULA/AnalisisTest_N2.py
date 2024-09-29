import pandas as pd
import matplotlib.pyplot as plt
from tkinter import simpledialog
import tkinter as tk


def cargarData(file_path):
    """Load the Excel file and return the DataFrame."""
    return pd.read_excel(file_path, "T")

def columnas(dataFrame):
    """Plot the distribution of scores as a bar chart."""
    puntuacion = dataFrame['Puntuación']
    puntuacion_counts = puntuacion.value_counts()

    plt.figure(figsize=(8, 6))
    puntuacion_counts.plot(kind='bar', color='green')
    plt.title('RELACION PUNTAJE CANTIDAD')
    plt.xlabel('Calificación Obtenida')
    plt.ylabel('Cantidad de Personas')
    plt.xticks(rotation=45)
    plt.ylim(0, puntuacion_counts.max() + 1)
    plt.yticks(range(0, puntuacion_counts.max() + 1, 1))
    plt.show()


def torta(dataFrame):
    """Plot a pie chart showing the distribution of responses to a question"""
    columnaAnalizada = dataFrame['En SIMULA, ¿qué palabra clave se utiliza para definir una clase?']
    columnaAnalizada_counts = columnaAnalizada.value_counts()
    plt.figure(figsize=(8, 8))
    columnaAnalizada_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#99ff99', '#ff6666', '#99ff98'])
    plt.title('En SIMULA, ¿qué palabra clave se utiliza para definir una clase?')
    plt.xlabel('DIAGRAMA DE TORTA')
    plt.ylabel('')
    plt.show()


def dispersion(dataFrame):
    """Plot a scatter plot """
    x_column = dataFrame['¿Qué tipo de estructura de datos se utiliza en SIMULA para implementar una lista enlazada?']
    y_column = range(len(x_column))
    plt.figure(figsize=(7, 4))
    plt.scatter(x_column, y_column, color='grey', alpha=0.6)
    plt.title('¿Qué tipo de estructura de datos se utiliza en SIMULA para implementar una lista enlazada?')
    plt.xlabel('Tipo de Estructura de Datos')
    plt.ylabel('Puntos representativos a cada persona')
    plt.xticks(rotation=45)  # Rotar etiquetas del eje X si es necesario
    plt.grid(True)
    plt.yticks([])
    plt.show()

def main():
    excelPath = r"SIMULA(respuestas).xlsx"
    dataFrame = cargarData(excelPath)

    root = tk.Tk()
    root.withdraw()
    options = {
        "1": "Ver la cantidad de estudiantes por la nota obtenida",
        "2": "En SIMULA, ¿qué palabra clave se utiliza para definir una clase?",
        "3": "¿Qué tipo de estructura de datos se utiliza en SIMULA para implementar una lista enlazada?",
        "4": "Salir"
    }

    while True:
        # Mostrar el menú
        option = simpledialog.askstring("Selecciona el gráfico",
                                        "Selecciona una opción:\n" + "\n".join(
                                            [f"{k}: {v}" for k, v in options.items()]))

        if option == "1":
            columnas(dataFrame)
        elif option == "2":
            torta(dataFrame)
        elif option == "3":
            dispersion(dataFrame)
        elif option == "4":
            break
        else:
            simpledialog.messagebox.showerror("Error", "Opción no válida. Intenta nuevamente.")
main()