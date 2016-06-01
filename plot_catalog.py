import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii



tbl = ascii.read("simple_table.csv")
tbl

tbl["ra"]

import astropy.coordinates as coord
import astropy.units as u

first_row = tbl[0]  # get the first (0th) row
ra = coord.Angle(first_row["ra"], unit=u.hour)  # create an Angle object
ra.degree  # convert to degrees

# New table
tbl = ascii.read("Young-Objects-Compilation.csv")
tbl.colnames
tbl[0]

# Try again
tbl = ascii.read("Young-Objects-Compilation.csv", header_start=1)
tbl.colnames

# And again
tbl = ascii.read("Young-Objects-Compilation.csv", header_start=1, data_start=2)
print(tbl['RA'])
tbl['RA'].filled(np.nan)
# Can't print these out because there are unicode characters in the references and notes


data = ascii.read("Young-Objects-Compilation.csv", header_start=1, data_start=2)

plt.scatter(data["Jmag"] - data["Kmag"], data["Jmag"]) # plot J-K vs. J
plt.ylim(reversed(plt.ylim())) # flip the y-axis
plt.xlabel("$J-K_s$", fontsize=20)
plt.ylabel("$J$", fontsize=20)


import astropy.coordinates as coord
ra = coord.Angle(data['RA'].filled(np.nan)*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(data['Dec'].filled(np.nan)*u.degree)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)