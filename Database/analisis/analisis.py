import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y lo guarda en la variable 'df'. Lo lee
df = pd.read_csv("01_semiconductor_trade_flows.csv")

print("OKEY! archivo cargado correctamente")

# Muestra en la terminal las primeras 5 filas (para entender cómo vienen los datos)
print(df.head())

# '.shape' devuelve una tupla con (filas, columnas). Las guardamos en variables separadas
filas, columnas = df.shape

# Muestra el tamaño total de la tabla original
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

total_anios = df['year'].count()

filtro_avanzado = df['hardware_type'].str.startswith('Advance', na=False)
# .str.startswith('Advance') busca en 'hardware_type' textos que empiecen con "Advance".
# "na=False" si hay celdas vacías las ignora 

# Aplicamos el filtro: 'df_filtrado' ahora es una NUEVA tabla SOLO con tecnología avanzada
df_filtrado = df[filtro_avanzado]

total_registros = df_filtrado['hardware_type'].count()

# .sum() suma todos los valores de la columna de dinero, pero SOLO de la tabla filtrada
suma_dinero = df_filtrado['trade_value_usd_millions'].sum()


print("-----Reporte automatizado-----")
print(f"Monto total: USD {suma_dinero:.2f} millones") # ".2f" hace que se muestre el dinero con solo 2 decimales


# Preguntamos el dinero total para decidir qué mensaje mostrar:

# Si supera los 500 millones
if Default_limite_alto := (suma_dinero > 500): # El ':=' evalúa la condición y crea la variable a la vez (operador morsa)
    print("Alerta: El volumen de mercado es de critico y de alta prioridad")
    print("Requiere revision inmediata")

# Si no superó los 500, pero sí es mayor a 200 millones
elif suma_dinero > 200:
    print("Aviso: volumen mercado moderado/alto")
    print("Monitorear comportamiento proximo trimestre")

# Si es igual o menor a 200 millones
else:
    print("Estado: volumen del mercado bajo o dentro del parametro")
    print("No se requiere accion adicional")


#--------------------------------------------
# GRAFICO 1: Grafico de Barras (con Seaborn)
#--------------------------------------------

print("\n Generando Grafico de Barras ")
sns.set_theme(style="whitegrid") # Configura el estilo de la grilla a blanca

plt.figure(figsize=(9,5))

sns.barplot(data=df,
            x="hardware_type",
            y="trade_value_usd_millions",
            estimator=sum,
            errorbar=None,
            palette="Blues_d")

plt.title("Distribuición economica de tecnologia avanzada", fontsize=14)
    
plt.xlabel("Tipo de Hardware", fontsize=11)
plt.ylabel("Total (millones USD)", fontsize=11)

plt.tight_layout()
plt.xticks(rotation=25, fontsize=6) #Rota y cambia el tamaño de los nombres de titulos de cada elemento representado
plt.savefig("grafico_barras.png", dpi=300)
plt.close()
print("Grafico de barras guardado exitosamente")

#--------------------------------------------
# GRAFICO 2: Grafico de Tortas (con Seaborn)
#--------------------------------------------

print("\n Generando grafico de torta")

datos_torta=(df.groupby("hardware_type")["trade_value_usd_millions"].sum().nlargest(5))

plt.figure(figsize=(7,7))
plt.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2")[0:5],
    startangle=140,
    wedgeprops={'edgecolor':'white','linewidth':2}
)

plt.title("Distribuicion interna: Tecnologia Avanzada", fontsize=14)
plt.tight_layout()
plt.savefig("grafico_tortas.png", dpi=300)
plt.close()
print("Grafico de tortas guardado exitosamente")

#--------------------------------------------
# GRAFICO 3: Grafico de Tortas (con Seaborn) (MODIFICAR: hacer 2 (o 1?) graficos siguiendo la misma logica anterior pero con otro elemento de la tabla)
#--------------------------------------------

print("\n Generando grafico de torta")

datos_torta=(df.groupby("hardware_type")["trade_value_usd_millions"].sum().nlargest(5))

plt.figure(figsize=(7,7))
plt.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2")[0:5],
    startangle=140,
    wedgeprops={'edgecolor':'white','linewidth':2}
)

plt.title("Distribuicion interna: Tecnologia Avanzada", fontsize=14)
plt.tight_layout()
plt.savefig("grafico_tortas.png", dpi=300)
plt.close()
print("Grafico de tortas guardado exitosamente")