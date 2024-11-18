import csv
import json
import copy
import os

for i in range(10):
    instance = {}
    instance['services'] = {}
    instance['stations'] = ['Retiro','Tigre']
    instance['cost_per_unit'] = {'Tigre' : 1.0, 'Retiro' : 1.0}


    filename = os.path.join(os.path.dirname(__file__), f'demanda_alta/instancia{i+1}')
    # Open the CSV file in read mode
    with open(filename + '.csv', 'r') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        # Loop through each row in the CSV file
        for row in csvreader:
            # Each row is a list of values, you can access them by index
            #print(row)
            service_id = row[0]
            instance['services'][service_id] = {}
            dep = {'time': int(row[1]), 'station':str(row[2]), 'type':str(row[3])}
            arr = {'time': int(row[4]), 'station':str(row[5]), 'type':str(row[6])}
            instance['services'][service_id]['stops'] = copy.deepcopy([dep,arr])
            instance['services'][service_id]['demand'] = [int(row[7])]



    instance['rs_info'] = {'capacity': 100, 'max_rs': 6}
    instance['rs_info'] = {'capacity': 100, 'max_rs': 25}
    #pprint.pprint(instance)

    with open(filename + '.json', 'w') as json_file:
        json.dump(instance, json_file)