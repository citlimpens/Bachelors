#Pyplot 
#importar todos los paqueres


import numpy as np 
np.set_printoptions(precision=4, supress=True)
import io
from pandas import Series, DataFrame
import pandas as pd 
import matplotlib.pyplot as plt 
plt.rc('figure', figsize=(2,10))
"""
PAra mostrar la gráfica en una nueva pestaña, se puede usar:
plt.show()
Para que se muestre en la siguiente lindea se usa:
% matplotlib inline

"""
from numpy.random import randn

#Grafico de lineas

x1 = np.arange(0, 20, 0.1);
y1 = np.sin(x1)

plt.plot(x1,(-x1))

#La linea por default es recta y azul, se puede cambiar, todas las opcines en manual

plt.plot(x1, (-x1), "r--")

#seno de x1
plt.plot(x1,y1)

#En vez de plot, se puede usar scatter, y tiene más funciones
#También se pueden ordenar las matrices como se gusta
#Se define la figura grande, la matriz de figuras
fig = plt.figure()
#se define cada una de las figuras en su sitio, y después se define como es cada una
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)

plt.plot(ranndn(50).cumsum(), 'k--')
_=x1.hist(randn(100), bins=20,color='k',alpha=0.3)
x2.scatter(np.arange(30),np.arange(30)+3*randn(30))


#PAra bajar los datos
from urllib import request
import shutil

url = 'http://fenixrepo.fao.org/cdn/data/flude/download/BULK.zip'
file_name = 'BULK.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
	shutil.copyfileobj(response, out_file)

#este solo sirve para comprobar si el archivo sí es zip
import zipfile as zp 
zp.is_zipfile("BULK.zip")
#Te puede poner una lista de los archivos en ese zip y extraer los que quieras













