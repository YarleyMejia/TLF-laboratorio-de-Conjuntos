import pandas as pd
import matplotlib.pyplot as plt


excelPath = r"SIMULA(respuestas).xlsx"
dataFrame = pd.read_excel(excelPath, "T")


print(dataFrame.head())
print(dataFrame.columns)


puntuacion = dataFrame['Puntuación']
puntuacion_counts = puntuacion.value_counts()

# Gráfico de columnas
plt.figure(figsize=(8, 6))
puntuacion_counts.plot(kind='bar', color='green')
plt.title('RELACION PUNTAJE CANTIDAD')
plt.xlabel('Calificación Obtenida')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45)

plt.ylim(0, puntuacion_counts.max() + 1)
plt.yticks(range(0, puntuacion_counts.max() + 1, 1))


palabraClave = dataFrame['En SIMULA, ¿qué palabra clave se utiliza para definir una clase?']
palabraClave_counts = palabraClave.value_counts()


plt.figure(figsize=(8, 8))
palabraClave_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#99ff99','#ff6666','#99ff98'])
plt.title('En SIMULA, ¿qué palabra clave se utiliza para definir una clase?')
plt.ylabel('')  # Para quitar la etiqueta del eje y
plt.show()
