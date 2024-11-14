from railway_service import *
import os

##################
# CARGAR LA DATA #
##################

file_name = os.path.join(os.path.dirname(__file__), '../instances/toy_instance.json')
#file_name = os.path.join(os.path.dirname(__file__), '../test/catch_and_shoot.json')
#file_name = os.path.join(os.path.dirname(__file__), '../test/descordinados.json')
#file_name = os.path.join(os.path.dirname(__file__), '../instances/pilar_cabred_semana.json')
#file_name = os.path.join(os.path.dirname(__file__), '../test/one_sends.json')
data = load_instance(file_name)

###########################################
# RESOLVER USANDO EL MÉTODO DE LA EMPRESA #
###########################################
unidades_nuevas, stock = modelo_empresa(data)
print("stock: ", stock)
print("Unidades nuevas: ", unidades_nuevas)

############################################################
# CREAR Y MOSTRAR EL GRAFO COMO SE PROPONE EN EL ENUNCIADO #
############################################################
grafo, nodos_estacion = create_graph(data)
#show_graph(grafo, data, nodos_estacion)

###################################################################################
# RESOLVER EL PROBLEMA COMO PROBLEMA DE CIRCULACIÓN Y MOSTRAR EL FLUJO RESULTANTE #
###################################################################################
circulacion = solve_circulacion(grafo)
cost = get_cost(grafo, circulacion, nodos_estacion)
print("Costo de la circulación: ", cost)
#show_flow(grafo, circulacion, data, nodos_estacion)