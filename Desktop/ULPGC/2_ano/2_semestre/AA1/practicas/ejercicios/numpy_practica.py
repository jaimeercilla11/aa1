import numpy as np

# 1
m = np.zeros(10)
m[4] = 1
print(m)

# 2
v = np.random.randint(10,49, size = 10)
print(v)

# 3
v2 = np.random.randint(0,8, size = (3,3))
print(v2)

# 4 
v3 = np.zeros((4,4))
for i in range(4):
    v3[i, i] = 1
print (v3)

# 5
v4 = np.random.random((3,3,3))
print(v4)

# 6
v5 = np.zeros((5,5))
v5[0, :] = 1
v5[-1, :] = 1
v5[:,0] = 1
v5[:,-1] = 1
print(v5)


# 7 
v6 = np.random.random(size = 10)
print(v6)

valor_max = np.max(v6)
posicion = np.argmax(v6)
v6[posicion] = 0
print(v6)