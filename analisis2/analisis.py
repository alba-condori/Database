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

df_exacto = df[df['restaurant_type'] == 'Casual Dining']

print("Estos usuarios prefieren una cena casual:")
print(df_exacto)

filtro_avanzado = df['user_preferred_cuisine'].str.contains('chinese', na=False)
# .str.startswith('Advance') busca en 'hardware_type' textos que empiecen con "Advance".
# "na=False" si hay celdas vacías las ignora 

# Aplicamos el filtro: 'df_filtrado' ahora es una NUEVA tabla SOLO con tecnología avanzada
df_filtrado = df[filtro_avanzado]

print("Estos usuarios prefieren la comida china:")
print(df_filtrado)


columnas_clave = df_filtrado[['restaurant_name', 'restaurant_avg_orders_per_day']]
print("--- Columnas Clave de los usuarios que prefieren comida china ---")
print(columnas_clave.head())

suma_ordenes = df_filtrado['restaurant_avg_orders_per_day'].sum()
print(f"La suma del promedio de ordenes por dia es: {suma_ordenes}")

#df_clave_texto = df['restaurant_name']
#df_clave_numerico = df['restaurant_id']

#print(df_clave_texto.head())
#print(df_clave_numerico.head())

if Default_limite_alto := (suma_ordenes > 100000): # El ':=' evalúa la condición y crea la variable a la vez (operador morsa)
    print("Prioridad Alta")
    print("Restaurante Popular")

# Si es igual o menor a 100000 millones
else:
    print("Prioridad Normal")
    print("Restaurante Promedio")


#--------------------------------------------
# GRAFICO 1: Grafico de Barras (con Seaborn)
#--------------------------------------------

print("\n Generando Grafico de Barras ")
sns.set_theme(style="whitegrid") # Configura el estilo de la grilla a blanca

plt.figure(figsize=(9,5))

sns.barplot(data=df,
            x="day_of_week",
            y="restaurant_avg_orders_per_day",
            estimator=sum,
            errorbar=None,
            palette="Blues_d")

plt.title("Promedio de ordenes por dia en restaurantes", fontsize=14)
    
plt.xlabel("day_of_week", fontsize=11)
plt.ylabel("restaurant_avg_orders_per_day", fontsize=11)

plt.tight_layout()
plt.xticks(rotation=25, fontsize=6) #Rota y cambia el tamaño de los nombres de titulos de cada elemento representado
plt.savefig("grafico_barras.png", dpi=300)
plt.close()
print("Grafico de barras guardado exitosamente")



#--------------------------------------------
# GRAFICO 2: Grafico de Tortas (con Seaborn)
#--------------------------------------------

print("\n Generando grafico de torta")

datos_torta=(df.groupby("delivery_zone")["restaurant_delivery_time_avg"].sum().nlargest(5))

plt.figure(figsize=(7,7))
plt.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2")[0:5],
    startangle=140,
    wedgeprops={'edgecolor':'white','linewidth':2}
)

plt.title("Delivery", fontsize=14)
plt.tight_layout()
plt.savefig("grafico_tortas.png", dpi=300)
plt.close()
print("Grafico de tortas guardado exitosamente")

#-----------------------Actividad-9--------------------------

# Reutilizamos nuestro filtro_avanzado y le sumamos una condición más
condicion_extra = df['restaurant_rating'] > 4
 
# Todo en una sola instrucción con .loc[]
resultado = df.loc[
    filtro_avanzado & condicion_extra,

    ['user_preferred_cuisine', 'restaurant_rating', 'restaurant_name']
]
 
print(resultado)
print(f'\nFilas seleccionadas: {len(resultado)}')

#-----------------------Actividad-10--------------------------
#terminar (remplazar las cosas y ENTENDER)

# Paso 1: diagnóstico
print('Nulos por columna:')
print(df.isnull().sum())
 
# Paso 2: introducir nulos si no hay (para practicar)
df_con_nulos = df.copy()
df_con_nulos.loc[[0, 3, 7], 'columna_numerica'] = None
 
# Paso 3: confirmar
print('\nNulos después de modificar:')
print(df_con_nulos.isnull().sum())
 
# Paso 4a: eliminar filas con nulos
df_sin_nulos = df_con_nulos.dropna()
 
# Paso 4b: reemplazar nulos con la media
media = df_con_nulos['columna_numerica'].mean()
df_rellenado = df_con_nulos.fillna({'columna_numerica': round(media, 2)})
 
# Paso 5: comparar
print(f'\nOriginal:   {len(df_con_nulos)} filas')
print(f'Con dropna: {len(df_sin_nulos)} filas  (se eliminaron filas)')
print(f'Con fillna: {len(df_rellenado)} filas  (se rellenaron los huecos)')

