#Para usar pandas se deben importar varios paquetes
% matplotlib inline

from __future__ import division
from numpy.random import randn
import numpy as np 
import os
import matplotlib.pyplot as plt 
import pandas as pd 
plt.rc('figure', figsize=(10,6))
np.set_printoptions(precision=4)

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]

#Tabla

from pandas import DataFrame, Series
import pandas as pd 
frame = DataFrame(records)
frame

#Tabla que solo aparecen los primeros 12

frame['tz'][:11]

#Conteo para cada uno de los diferentes tzs

tz_counts = frame['tz'].value_counts()
tz_counts[:11]

#Para poner algo en los valores que no hay nada = `perdidos" y los que no tienen valores ahi = "desconocidos"

clean_tz = frame['tz'].fillna('Perdido')
clean_tz[clean_tz == ' '] = 'Desconocido'
tz_counts = clean_tz.value_counts()
tz_counts[:11]

#graficas con pyplot barh = barras horizontales, rot = rotacion de los titulos, hay mas opcoones para colores y demas en matplot

plt.figure(figsize(10,4))

tz_counts[:10].plot(kind='barh', rot=0)