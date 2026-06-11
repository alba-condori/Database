import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y lo guarda en la variable 'df'. Lo lee
df = pd.read_csv("csao_session_dataset.csv")

print("OKEY! archivo cargado correctamente")

# '.shape' devuelve una tupla con (filas, columnas). Las guardamos en variables separadas
filas, columnas = df.shape

# Muestra el tamaño total de la tabla original
print(f"La tabla contiene {filas} filas y {columnas} columnas")


