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
plt.savefig("./Graficos/grafica_valor.png")
plt.show()

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