from railway_service import *
import os

f_out = open('resultados.csv', 'w')
f_out.write('archivo,costo_empresa,costo_circulacion\n')

for i in range(10):
    ##################
    # CARGAR LA DATA #
    ##################
    file_name = os.path.join(os.path.dirname(__file__), f'demandas_normales{i+1}.json')
    data = load_instance(file_name)

    ###########################################
    # RESOLVER USANDO EL MÉTODO DE LA EMPRESA #
    ###########################################
    costoA = modelo_empresa(data)
    
    ############################################
    # RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
    ############################################
    costoB = modelo_circulacion(data)

    f_out.write(f'demandas_normales{i+1},{costoA},{costoB}\n')