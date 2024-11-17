from railway_service import *
import os
import matplotlib.pyplot as plt
import numpy as np

f_out = open(os.path.join(os.path.dirname(__file__), f'demanda_alta/resultados.csv'), 'w')
f_out.write('archivo,costo_circulacion\n')
results_circulacion = []


for i in range(10):
    ##################
    # CARGAR LA DATA #
    ##################
    file_name = os.path.join(os.path.dirname(__file__), f'demanda_alta/instancia{i+1}.json')
    data = load_instance(file_name)
    
    ############################################
    # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
    ############################################
    costo = modelo_circulacion(data)
    results_circulacion.append(costo)

    f_out.write(f'instancia{i+1},{costo}\n')

f_out.close()

media = np.mean(results_circulacion)

medias = [14.1, 24.7, 34.2, 44.2]
tags = [500,1000,1500,2000]

plt.figure(figsize=(8, 5))
plt.plot(tags, medias, marker='o', linestyle='-', color='b')  # 'o' para puntos, '-' para la línea
plt.xlabel("Demanda media")
plt.ylabel("Unidades necesarias promedio")
plt.xticks(tags)
plt.title("Unidades necesarias promedio en función del tipo de demanda")
plt.grid()
plt.show()

print(media)