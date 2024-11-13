from railway_service import *
import os

############################################################
# CREAR Y MOSTRAR EL GRAFO COMO SE PROPONE EN EL ENUNCIADO #
############################################################
file_name = os.path.join(os.path.dirname(__file__), '../instances/toy_instance.json')
#file_name = os.path.join(os.path.dirname(__file__), '../test/catch_and_shoot.json')
data = load_instance(file_name)
grafo, nodos_estacion = create_graph(data)
#show_graph(grafo, data, nodos_estacion)

######################################################
# RESOLVER EL PROBLEMA Y MOSTRAR EL FLUJO RESULTANTE #
######################################################
circulacion = solve_circulacion(grafo)
cost = get_cost(grafo, circulacion, nodos_estacion)
print("Costo de la circulación: ", cost)
show_flow(grafo, circulacion, data, nodos_estacion)