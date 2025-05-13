#Generar datos y graficar una función Usa np.linspace() para generar valores x entre -10 y 10, y grafica y = x² - 3x + 2.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = x ** 2 - 3 * x + 2  
# Crear el gráfico
plt.plot(x, y, color='orange')
plt.title('Gráfico de la función y = x² - 3x + 2')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.savefig("Graficos/grafica_funcion.png")
plt.show()

#Comparación de funciones En el mismo gráfico, traza las funciones sin(x) y cos(x) para x entre 0 y 2π.

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Crear el gráfico
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('Gráfico de las funciones sin(x) y cos(x)')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.savefig("Graficos/grafica_funciones.png")
plt.show()

#Operaciones entre arrays Genera dos vectores de 100 valores aleatorios entre 0 y 100 y calcula:

# La suma total.
# El valor máximo.
# La desviación estándar.

import numpy as np
# Generar dos vectores de 100 valores aleatorios entre 0 y 100
vector1 = np.random.randint(0, 100, 100)
vector2 = np.random.randint(0, 100, 100)
# Calcular la suma total
suma_total = np.sum(vector1 + vector2)
# Calcular el valor máximo
maximo = np.max(vector1 + vector2)
# Calcular la desviación estándar
desviacion_estandar = np.std(vector1 + vector2)
# Imprimir los resultados
print(f"Suma total: {suma_total}")
print(f"Valor máximo: {maximo}")
print(f"Desviación estándar: {desviacion_estandar}")

#Histograma con NumPy Genera 1000 números aleatorios con distribución normal y muestra un histograma con plt.hist().
data = np.random.normal(loc=0, scale=1, size=1000)
# Crear el histograma
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title('Histograma de una Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.savefig("Graficos/grafica_histograma.png")
plt.show()

