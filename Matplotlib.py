#Escribe un programa que grafique la siguiente lista de valores: valores = [3, 7, 1, 5, 12] Agrega título, etiquetas de ejes y una cuadrícula

from matplotlib import pyplot as plt
import numpy as np


valores = [3, 7, 1, 5, 12]
x = np.arange(len(valores))
# Crear el gráfico de línea
plt.plot(x, valores, marker='o', color='blue')
plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.savefig("./Graficos/grafica_linea.png")




#Gráfico de barras Grafica la cantidad de estudiantes en 5 cursos:
cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
# Crear el gráfico de barras
plt.bar(cursos, cantidad, color='green')
plt.title('Cantidad de Estudiantes por Curso')
plt.xlabel('Cursos')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(axis='y')
plt.savefig("Graficos/grafica_cursos.png")
plt.show()

#Gráfico de dispersión (scatter plot) Genera dos listas de números aleatorios de 50 elementos y haz un gráfico de dispersión.

import random
x = [random.randint(1, 100) for _ in range(50)]
y = [random.randint(1, 100) for _ in range(50)]
# Crear el gráfico de dispersión
plt.scatter(x, y, color='red')
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.savefig("Graficos/grafica_dispersion.png")
plt.show()

#Subplots Crea un figure con 2 subgráficos:
# Uno con una línea senoidal.
# Otro con una función cuadrática

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = x ** 2
# Crear la figura y los subgráficos
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# Gráfico de la función senoidal
ax1.plot(x, y1, color='purple')
ax1.set_title('Función Senoidal')
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Seno')
ax1.grid(True)
# Gráfico de la función cuadrática
ax2.plot(x, y2, color='orange') 
ax2.set_title('Función Cuadrática')
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Cuadrado')
ax2.grid(True)
plt.tight_layout()
plt.savefig("Graficos/grafica_subplots.png")
plt.show()



