# Working with Tables
import numpy as np
from astropy.table import Table
from astropy.units import imperial

data = np.genfromtxt('text_data.txt', delimiter=',')

t = Table(data, names=['x', 'y'])
t['x']
t['x'][2]
t[2]
t[0:3]
t['x'].unit = 'km'
t['x'].to(imperial.mile)

len(t)
t.colnames

# Make a new column
t['z'] = t['x'] + t['y']

# Save it
from astropy.io import ascii
ascii.write(t, 'modified.txt', format='csv')