from railway_service import *
import os
import numpy as np
import time

cantidades = [5000]
tiempos = []
#f_out = open(os.path.join(os.path.dirname(__file__), f'resultados.csv'), 'w')
#f_out.write('cantidad,tiempo\n')
for cantidad in cantidades:
    ts = []
    for i in range(5):
        ##################
        # CARGAR LA DATA #
        ##################
        file_name = os.path.join(os.path.dirname(__file__), f'{cantidad}.json')
        data = load_instance(file_name)
        
        ##############################################################
        # RESOLVER USANDO EL MODELO DE CIRCULACIÓN Y TOMAR EL TIEMPO #
        ##############################################################
        a = time.perf_counter()
        costo = modelo_circulacion(data)
        b = time.perf_counter()
        ts.append(b-a)
        if i == 0:
            print(b-a)
    tiempos.append(np.mean(ts))
    #f_out.write(f'{cantidad},{np.mean(ts)}\n')

#f_out.close()
print(tiempos)

