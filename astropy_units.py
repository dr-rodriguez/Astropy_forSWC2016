# Using units with astropy
from astropy import units as u

distance = 72 * u.parsec

print(distance.to(u.lightyear))

velocity = 14 * u.km / u.second

time = distance / velocity

time = time.to(u.year)

print(time)

from astropy import constants as const

print(const.c)

print(const.c.to('km/s'))

print(velocity/const.c.to('km/s'))

