f = open('descordinados.csv', 'r')
f_out = open('descordinados2.csv', 'w')


for line in f:
    aux = line.replace(';',',')
    f_out.write(aux)

f.close()
f_out.close()
