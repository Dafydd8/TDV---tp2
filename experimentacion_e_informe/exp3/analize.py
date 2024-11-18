import sys
import os
directorio = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(directorio)
from railway_service import *
import matplotlib.pyplot as plt
import numpy as np

cotas = [25,20,15,10]
medias_cota = []
for cota in cotas:
    f_out = open(os.path.join(os.path.dirname(__file__), f'cota_{cota}/resultados.csv'), 'w')
    f_out.write('archivo,costo_circulacion\n')
    results_circulacion = []
    for i in range(10):
        ##################
        # CARGAR LA DATA #
        ##################
        file_name = os.path.join(os.path.dirname(__file__), f'cota_{cota}/instancia{i+1}.json')
        data = load_instance(file_name)
        
        ############################################
        # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
        ############################################
        costo = modelo_circulacion(data)
        results_circulacion.append(costo)
        f_out.write(f'instancia{i+1},{costo}\n')
        
    f_out.close()
    media = np.mean(results_circulacion)
    medias_cota.append(media)

print(medias_cota)