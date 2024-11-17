import numpy as np
import os

for i in range(1, 11):
    filename = os.path.join(os.path.dirname(__file__), f'demanda_alta/instancia{i}.csv')
    f_out = open(filename, 'w')
    f_out.write('service id,hora,origen,tipo,hora,destino,tipo,demanda (pax)\n')

    horarios = []
    for i in range(5):
        horarios.append(300+i*120+np.random.randint(-30, 30))
    for i in range(5):
        horarios.append(300+i*120+np.random.randint(-30, 30))
    a = np.random.normal(2000, 200, 10)
    demandas = []
    for elem in a:
        if elem < 0:
            demandas.append(0)
        elif elem > 2500:
            demandas.append(2500)
        else:
            demandas.append(int(elem))

    id = 0
    while(id < 10):
        f_out.write(f'{id},{horarios[id]},Retiro,D,{horarios[id]+24},Tigre,A,{demandas[id]}\n')
        f_out.write(f'{id+1},{horarios[id+1]},Tigre,D,{horarios[id+1]+24},Retiro,A,{demandas[id+1]}\n')
        id+=2

    f_out.close()