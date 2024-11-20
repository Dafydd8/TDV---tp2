from railway_service import *
import os

##################
# CARGAR LA DATA #
##################
#file_name = os.path.join(os.path.dirname(__file__), '../test/catch_and_shoot.json')
#file_name = os.path.join(os.path.dirname(__file__), '../test/descordinados.json')
#file_name = os.path.join(os.path.dirname(__file__), '../instances/pilar_cabred_semana.json')
file_name = os.path.join(os.path.dirname(__file__), '../test/salidas_simultaneas.json')
data = load_instance(file_name)

###########################################
# RESOLVER USANDO EL MÉTODO DE LA EMPRESA #
###########################################
costo = modelo_empresa(data)
print("Con el modelo de la empresa se necesitan: ", costo, " unidades")

############################################
# RESOLVER USANDO EL MODELO DE CIRCULACIÓN #
############################################
costo = modelo_circulacion(data)
print("Con el modelo de circulación se necesitan: ", costo, " unidades")