#Para usar pandas se deben importar varios paquetes
from _future_ import division
from numpy.random import randn
import numpy as np 
import od
import matplotlib.pyplot as plt 
import pandas as pd 
plt.rc('figure', figsize=(10,6))
np.set_printoptions(precision=4)

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]

from pandas import DataFrame, Series
import pandas as pd 
frame = DataFrame(records)
frame

frame['tz'][:11]