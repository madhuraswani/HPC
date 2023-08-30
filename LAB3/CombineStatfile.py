import os
import re
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

stat_files=os.listdir("./stats")

data={}
fields=["Branch Predictor","Freq","BlockSize"]
for feild in fields:
    data[feild]=[]
# for file in stat_files:
stats=["simSeconds","hostInstRate","board.processor.cores.core.branchPred.lookups","board.processor.cores.core.branchPred.condPredicted","board.processor.cores.core.branchPred.BTBHitRatio","board.processor.cores.core.commit.branchMispredicts"]
for stat in stats:
    data[stat]=[]


for f in stat_files:
    param=f.split("_")[1]
    params=param.split("-")
    for feild,param in zip(fields,params):
        if param.endswith(".txt"):
                    data[feild].append(param[:-4])
        else:
                    data[feild].append(param)
    with open("./stats/"+f) as file:
        for line in file:
            for stat in stats:
                if line.__contains__(stat):
                    data[stat].append(float(re.search("\d+\.*\d*",line.split(stat)[1])[0]))
    print(data)


data=pd.DataFrame.from_dict(data)

data.to_csv('Combined_data.csv')