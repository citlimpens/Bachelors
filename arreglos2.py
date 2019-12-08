import numpy as np 
from numpy.random import randn
arr = np.arange(10)

np.save("some_array", arr)
np.load("some_array.npy")

"""
#Se pueden guardar como zip con:
np.savez("nombre del archivo.npz", a= lo que vaya ahi, b = el otro archivo)
se pueden pedir esos archivos
arhivos = no.load("nombredel archivo.npz")
archivos[archivo especifico que se quiera abrir dentro del zip]
"""