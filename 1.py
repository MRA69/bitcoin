import pandas as pd
df = pd.read_csv('mempool.csv')
df.columns =[column.replace(" ", "_") for column in df.columns]
df = df[df['parents_'] >= ' ']
print(df['parents_'])
kf = df.head(2000)
print(kf['tx_id'])