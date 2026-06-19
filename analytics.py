import pandas as pd
df=pd.read_csv('sensor_data.csv')
print('Average Temperature:',df['temperature'].mean())
print('Maximum Temperature:',df['temperature'].max())
print(df[df['machine_status']=='Critical'])
