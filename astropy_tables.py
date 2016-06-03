# Working with Tables
import numpy as np
from astropy.table import Table
from astropy.units import imperial

data = np.loadtxt('text_data.txt', delimiter=',')

t = Table(data, names=['x', 'y'])


import matplotlib.pyplot as plt
plt.plot(t['x'], t['y'], marker='o', linestyle='')
plt.show()

from astropy import units as u
t['x']
t['x'][2]
t[2]
t[0:3]
t['x'].unit = 'km'
t['x'].to(imperial.mile)

len(t)
t.colnames

# Make a new column
t['c'] = t['x'].to(imperial.mile)
t['z'] = t['x'] + t['y']

# Save it
from astropy.io import ascii
ascii.write(t, 'modified.txt', format='csv')
t2 = ascii.read('modified.txt')