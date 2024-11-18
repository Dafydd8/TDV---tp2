import sys
import os
directorio = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(directorio)
from railway_service import *
import matplotlib.pyplot as plt

f_out = open(os.path.join(os.path.dirname(__file__), f'resultados.csv'), 'w')
f_out.write('instancia,costo_1,costo_2,proporcion,demanda_media\n')
proporciones = {}

for tipo in ['baja', 'alta']:
    props = []
    for i in range(10):
        rtas = []
        for j in range(2):
            ##################
            # CARGAR LA DATA #
            ##################
            file_name = os.path.join(os.path.dirname(__file__), f'media_{tipo}/costo{j+1}_{i+1}.json')
            data = load_instance(file_name)
            
            ############################################
            # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
            ############################################
            costo = modelo_circulacion(data)
            rtas.append(costo)
            
        f_out.write(f'{i+1},{rtas[0]},{rtas[1]},{rtas[1]/rtas[0]},{tipo}\n')
        props.append(rtas[1]/rtas[0])
    proporciones[tipo] = props

print(proporciones)
plt.figure(figsize=(8, 6))
plt.boxplot([proporciones["baja"], proporciones["alta"]], labels=["500", "1800"])
plt.xlabel("Demanda media")
plt.ylabel("Cociente")
plt.title("Cociente de unidades necesarias para configuraciones de costo 1 y 2, según demanda")
plt.grid()
plt.show()

print(proporciones)
f_out.close()
