import pandas as pd
import numpy as np

# 2 
df = pd.read_csv('C:/Users/ercil/Desktop/ULPGC/2_ano/2_semestre/AA1/practicas/datos-practica-2/iris-perdidos.csv')
variables = df.columns
for variable in variables[:-1]:
    media = df[variable].mean()  
    df[variable] = df[variable].fillna(media)

print(df.head(10))

# 3 
from sklearn.preprocessing import MinMaxScaler
datos = df.values
variables = datos[:,:-1]
variables
normalizador = MinMaxScaler()
normalizador.fit(variables)
res = normalizador.transform(variables)
print(res)

# 4
from sklearn.preprocessing import LabelEncoder

dic = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2} # diccionario para mapear las clases
for i in range(len(df)): # transformamos las clases a valores numéricos
    df.loc[i,'class'] = dic[df.iloc[i]['class']]
    conversor = LabelEncoder()
conversor.fit(df['class'])
res = conversor.transform(df['class'])
print(res)
