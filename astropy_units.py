# Using units with astropy
from astropy import units as u

distance = 72 * u.parsec

print(distance.to(u.lightyear))

velocity = 14 * u.km / u.second

time = distance / velocity

time = time.to(u.year)

print(time)

print('The amount of time (in {0}) to travel '
      '{1.value} {1.unit} is {2:.0f} ({2:.3g})'.format(time.unit, distance, time.value))

from astropy import constants as const

print(const.c)

print(const.c.to('km/s'))

print(velocity/const.c.to('km/s'))

