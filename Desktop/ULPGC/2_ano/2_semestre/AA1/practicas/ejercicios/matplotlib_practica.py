import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# 1
x = np.linspace(-10, 10, num= 100)
y = 1/(x**2 + 1)
plt.plot(x,y)
plt.show()

# 2
x = np.linspace(-10, 10, num= 100)
y = 1/(x**2 + 1)
plt.plot(x,y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 3
x = np.linspace(-10, 10, num= 100)
y = 1/(x**2 + 1)
y2 = 1/(np.e**-x + 1)
plt.plot(x,y, 'b', x, y2, 'r')
plt.grid()
plt.show()

# 4
df = pd.read_csv("coches.csv")
plt.scatter(df['kms'], df['precio'], color = 'black')
plt.grid()
plt.xlabel('kms')
plt.ylabel('precio')
plt.show()

# 5
marcas = df['marca'].value_counts()
plt.figure(figsize=(8,5))
marcas.plot(kind='bar', color='blue', edgecolor='black')
plt.show()
