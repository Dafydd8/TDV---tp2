from railway_service import *
import os
import matplotlib.pyplot as plt
import numpy as np

f_out = open(os.path.join(os.path.dirname(__file__), f'media_alta/resultados.csv'), 'w')
f_out.write('archivo,costo_empresa,costo_circulacion\n')
results_empresa = []
results_circulacion = []


for i in range(10):
    ##################
    # CARGAR LA DATA #
    ##################
    file_name = os.path.join(os.path.dirname(__file__), f'media_alta/demandas_normales{i+1}.json')
    data = load_instance(file_name)

    ###########################################
    # RESOLVER USANDO EL MÉTODO DE LA EMPRESA #
    ###########################################
    costoA = modelo_empresa(data)
    results_empresa.append(costoA)
    
    ############################################
    # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
    ############################################
    costoB = modelo_circulacion(data)
    results_circulacion.append(costoB)

    f_out.write(f'demandas_normales{i+1},{costoA},{costoB}\n')

f_out.close()

diferencias = []
for i in range(10):
    empresa = results_empresa[i]
    circulacion = results_circulacion[i]
    dif = empresa - circulacion
    diferencias.append(dif)

etiquetas = [f"Instancia {i+1}" for i in range(len(diferencias))]

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(etiquetas, diferencias)
plt.xlabel("Instancias")
plt.ylabel("Solución Empresa - Solución Circulación")
plt.title("Diferencia entre la solución de la empresa y la solución de circulación")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()