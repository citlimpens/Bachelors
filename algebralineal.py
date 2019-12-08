import numpy as np 
from numpy.random import randn

#multiplicacion de matrices
x = np.array([[1.,2.,3.],[4.,5.,6.]])
print(x)

y = np.array([[6.,23.],[-1.,7.],[10.,2.]])
print(y)

mult = x.dot(y)
print(mult)

np.random.seed(12345)

from numpy.linalg import inv, qr
X = randn(5,5)
print(X)

#matriz traspuesta y luego multiplicada por la original
mat = X.T.dot(X)
print(mat)

#la inversa
inversa = inv(mat)
print(inversa)