import pandas as pd

# Lee el archivo CSV de comercio de semiconductores y lo guarda en la variable 'df'
df = pd.read_csv("01_semiconductor_trade_flows.csv")

print("OKEY! archivo cargado correctamente")

# Muestra en la terminal las primeras 5 filas (para entender cómo vienen los datos)
print(df.head())

# '.shape' devuelve una tupla con (filas, columnas). Las guardamos en variables separadas
filas, columnas = df.shape

# Muestra el tamaño total de la tabla original
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

total_anios = df['year'].count()

# .str.startswith('Advance') busca en 'hardware_type' textos que empiecen con "Advance".
# "na=False" si hay celdas vacías las ignora 
filtro_avanzado = df['hardware_type'].str.startswith('Advance', na=False)

# Aplicamos el filtro: 'df_filtrado' ahora es una NUEVA tabla SOLO con tecnología avanzada
df_filtrado = df[filtro_avanzado]

total_registros = df_filtrado['hardware_type'].count()

# .sum() suma todos los valores de la columna de dinero, pero SOLO de la tabla filtrada
suma_dinero = df_filtrado['trade_value_usd_millions'].sum()


print("-----Reporte automatizado-----")
# ':.2f'hace que se muestre el dinero con solo 2 decimales
print(f"Monto total: USD {suma_dinero:.2f} millones")


# Evaluamos el dinero total para decidir qué mensaje mostrar en consola:

# Si supera los 500 millones.
if Default_limite_alto := (suma_dinero > 500): # El ':=' evalúa la condición y crea la variable a la vez (operador morsa)
    print("Alerta: El volumen de mercado es de critico y de alta prioridad")
    print("Requiere revision inmediata")

# Si no superó los 500, pero sí es mayor a 200 millones.
elif suma_dinero > 200:
    print("Aviso: volumen mercado moderado/alto")
    print("Monitorear comportamiento proximo trimestre")

# Si es igual o menor a 200 millones.
else:
    print("Estado: volumen del mercado bajo o dentro del parametro")
    print("No se requiere accion adicional")