import pandas as pd
import numpy as np


df = pd.read_csv(r'../Datasets/Pokemon.csv')


df.head(10)


df.iloc[5]


df.iloc[5, 1]


df.loc[5, 'Type 1']


pivote = pd.pivot_table(df, values=['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], index='Type 1', aggfunc=np.mean)

pivote


legendarios = df[df['Legendary'] == True]

legendarios
