import pandas as pd
df = pd.read_csv('mempool.csv')
df.columns =[column.replace(" ", "_") for column in df.columns]
sf = df[df['parents_'] >= ' ']
print(sf['parents_'])
kf = sf.head(2000)
print(kf['tx_id'])

"""
***THIS IS THE ACTUAL LONG VERSION WHICH IS TOTALLY NOT CLEAR ON TERMINAL******
import pandas as pd
df = pd.read_csv('mempool.csv')
df.columns =[column.replace(" ", "_") for column in df.columns]
sf = df[df['parents_'] > ' ']
print(sf['parents_'].to_string())
kf = sf.head(2000)
print(kf['tx_id'].to_string())
"""
