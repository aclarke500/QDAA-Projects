import pandas as pd

df = pd.read_csv('data.csv')
df.drop(columns=['Name', "Queen's Email"], inplace=True)

df.to_csv('data.csv', index=False)