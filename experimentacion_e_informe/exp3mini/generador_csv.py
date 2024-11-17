import numpy as np

for i in range(1, 11):
    filename = f'demandas_normales{i}.csv'
    f_out = open(filename, 'w')
    f_out.write('service id,hora,origen,tipo,hora,destino,tipo,demanda (pax)\n')

    horarios = np.random.randint(300, 400, 4)
    demandas = [2000]*4

    id = 0
    while(id < 4):
        f_out.write(f'{id},{horarios[id]},Retiro,D,{horarios[id]+30},Tigre,A,{demandas[id]}\n')
        f_out.write(f'{id+1},{horarios[id+1]},Tigre,D,{horarios[id+1]+30},Retiro,A,{demandas[id+1]}\n')
        id+=2

    f_out.close()