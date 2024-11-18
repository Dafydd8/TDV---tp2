import sys
import os
directorio = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(directorio)
from railway_service import *
import matplotlib.pyplot as plt
import numpy as np

demandas_medias = [500,1000,1500,2000]
tipos = {500:'baja', 1000:'media-baja', 1500:'media-alta', 2000:'alta'}
medias = []

for m in demandas_medias:
    f_out = open(os.path.join(os.path.dirname(__file__), f'demanda_{tipos[m]}/resultados.csv'), 'w')
    f_out.write('archivo,costo_circulacion\n')
    results_circulacion = []
    for i in range(10):
        ##################
        # CARGAR LA DATA #
        ##################
        file_name = os.path.join(os.path.dirname(__file__), f'demanda_{tipos[m]}/instancia{i+1}.json')
        data = load_instance(file_name)
        
        ############################################
        # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
        ############################################
        costo = modelo_circulacion(data)
        results_circulacion.append(costo)

        f_out.write(f'instancia{i+1},{costo}\n')

    f_out.close()

    media = np.mean(results_circulacion)
    medias.append(media)

plt.figure(figsize=(8, 5))
plt.plot(demandas_medias, medias, marker='o', linestyle='-', color='b')  # 'o' para puntos, '-' para la línea
plt.xlabel("Demanda media")
plt.ylabel("Unidades necesarias promedio")
plt.xticks(demandas_medias)
plt.title("Unidades necesarias promedio en función del tipo de demanda")
plt.grid()
plt.show()

print(medias)