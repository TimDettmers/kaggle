import numpy as np
import pandas as p
from datetime import datetime
from util import Util
u = Util()
paths = ['/home/tim/Downloads/repair/RepairTrain.csv','/home/tim/Downloads/repair/SaleTrain.csv']

t1 = p.read_csv(paths[0])
t2 = p.read_csv(paths[1])

dict_sales = {}
for entry in t2.values:
    key = reduce(lambda x, y: str(x)+str(y),entry[:-1])
    if key in dict_sales:
        dict_sales[key][0] += entry[-1]
    else:
        dict_sales[key] = [entry[-1],entry[0],entry[1],entry[2]]

error_count = 0
dict_repair = {}
for entry in t1.values:
    key = reduce(lambda x, y: str(x)+str(y),entry[:3])
    if key in dict_sales:
        timespan = datetime.strptime(entry[3],'%Y/%m') - datetime.strptime(dict_sales[key][-1],'%Y/%m')
        repair_key = key + entry[3]
        sales = dict_sales[key][0]
        if repair_key not in dict_repair:
            dict_repair[repair_key] = [entry[-1],timespan.days,entry[0],entry[1],entry[2],entry[3],sales]
        else:
            dict_repair[repair_key][0] += entry[-1]
    else:
       error_count += 1

data = []
for value in dict_repair.values():
    data.append([ele for ele in value])

X =  np.array(data)
X = X[:,[0,1,2,3,6]]

fac1 = u.strings_to_classes(X[:,2])
fac2 = u.strings_to_classes(X[:,3])

t1 = u.create_t_matrix(fac1)
t2 = u.create_t_matrix(fac2)

X = np.hstack([np.float32(X[:,[0,1,4]]),t1,t2])
print X.shape

np.save('/home/tim/Downloads/repair/train.npy',X)
print 'Saved!'

#TODO: use util to create categories
#print(t1.ix[0:5,:])
#print(t2.ix[0:5,:])

#print data



