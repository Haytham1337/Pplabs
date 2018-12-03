import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
with open("DataSet.csv",'r') as file:
    data=pd.read_csv(file)
    #print(data.iloc[:10],end="\n\n")
    #print('Agency')
    #print(data["Agency"][:10])
    #print('\n\n Business Title')
    #print(data["Business Title"])
#data['Agency'].value_counts(sort = True).plot.bar()
#plt.show()
data['median'] = data.groupby('Salary Range From')['Salary Range To'].transform(np.median)
gb = data.groupby('Work Location')
data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
data1 = data1.median(axis=1)
data1.plot()
plt.show()







