import matplotlib.pyplot as plt
import csv

f = open('resultados.csv', 'r')
tiempos = []
for linea in csv.DictReader(f):
    tiempos.append(float(linea['tiempo']))

print(tiempos)

cantidades = [500,1000,2000,5000,10000,20000]

plt.figure(figsize=(10, 6))
plt.plot(cantidades, tiempos, marker='o', linestyle='-', color='b')
plt.xlabel("Eventos de salida por estación")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.title("Curva de Tiempo de Ejecución en Función del Tamaño de Entrada")
plt.grid()
plt.show()