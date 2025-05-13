#Lectura de archivos con Pandas Usa un archivo .csv llamado datos_ventas.csv con las siguientes columnas: Producto, Ventas, Precio, Fecha
from matplotlib import pyplot as plt
import pandas as pd
# Cargar el archivo CSV
df = pd.read_csv('datos_ventas.csv')

# Total de ventas (Ventas.sum())
total_ventas = df['Ventas'].sum()
# Promedio de precio
promedio_precio = df['Precio'].mean()
# Producto más vendido
producto_mas_vendido = df.loc[df['Ventas'].idxmax()]['Producto']

#Filtrar datos
#Muestra solo los productos vendidos en el mes de enero (Fecha empieza por 2025-01).
df['Fecha'] = pd.to_datetime(df['Fecha'])


#Gráfica de barras con Pandas
#Grafica la cantidad total vendida por producto. (Agrupa por Producto y suma las ventas).
df_grouped = df.groupby('Producto')['Ventas'].sum().reset_index()
df_grouped.plot(kind='bar', x='Producto', y='Ventas', color='blue')
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.grid(axis='y')
plt.savefig("Graficos/grafica_ventas_totales.png")
plt.show()