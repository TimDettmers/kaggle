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
data = []
for entry in t1.values:
    key = reduce(lambda x, y: str(x)+str(y),entry[:3])
    if key in dict_sales:
        timespan = datetime.strptime(entry[3],'%Y/%m') - datetime.strptime(dict_sales[key][-1],'%Y/%m')
        print timespan.days
        data.append([dict_sales[key],entry[-1],])
    else:
       error_count += 1
#print dict_sales
#print error_count
#TODO: use util to create categories
print(t1.ix[0:5,:])
print(t2.ix[0:5,:])

#print(dict_sales)



