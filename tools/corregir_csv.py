f = open('demandas_normales.csv', 'r')
f_out = open('demandas_normales2.csv', 'w')


for line in f:
    aux = line.replace(';',',')
    f_out.write(aux)

f.close()
f_out.close()
