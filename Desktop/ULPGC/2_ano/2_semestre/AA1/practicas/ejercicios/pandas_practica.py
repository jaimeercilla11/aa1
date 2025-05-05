import pandas as pd
import os
# 2
FOLDER = 'data/'
CHOCES_1 = os.path.join(FOLDER, 'coches.csv')

df = pd.read_csv("coches.csv")

print(df)
# 3
df2 = df.iloc[0:5]
df2[["marca", "modelo"]]

print(df2)

# 4
df3 = df["marca"]
print(df3.unique())

# 5
df5 = df[df['marca'] == 'Opel']
print(df5)

# 6 
marcas_unicas = df["marca"].unique()
for marca in marcas_unicas:
    filtro = df[df["marca"] == marca]
    kms_promedio = filtro["kms"].mean()
    print(f"{marca}: {kms_promedio}")


# 7 
df6 = df[df["año"] >= 2015]
print(df6.iloc[:,4] + 1000)