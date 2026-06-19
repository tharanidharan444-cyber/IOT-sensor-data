import pandas as pd, random
from datetime import datetime
data=[]
for i in range(100):
    data.append([f'S{100+i}',datetime.now(),random.randint(25,55),random.randint(40,90),random.choice(['Running','Warning','Critical'])])
pd.DataFrame(data,columns=['sensor_id','timestamp','temperature','humidity','machine_status']).to_csv('sensor_data.csv',index=False)
print('Dataset Generated Successfully')
