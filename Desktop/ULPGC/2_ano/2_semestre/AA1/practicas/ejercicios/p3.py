import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

FOLDER = 'C:/Users/ercil/Desktop/ULPGC/2_ano/2_semestre/AA1/practicas/datos-practica-3'
FILE = os.path.join(FOLDER,'tiempos-small.csv' )
SEED = 123
TEST_SIZE = 0.2

df = pd.read_csv(FILE, sep = ';')
df.head()
df.info()

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

x = [0,1,2]
plt.bar(x, regr.coef_)
plt.grid()
plt.show()