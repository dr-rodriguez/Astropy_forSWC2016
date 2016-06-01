# Read a FITS file image, examine header, plot image with WCS

from matplotlib import pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils.data import download_file

fits_file = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'
image_file = download_file(fits_file, cache=True )
hdu = fits.open(image_file)[0]  # [0] to select primary extension

# Header exploration
# hdu.info()  # if did not set [0] for hdu

hdu.header  # note that this is a dictionary
hdu.header.keys()
hdu.header.values()
hdu.header['DATE']
for key in hdu.header.keys():
    print(key, hdu.header[key])

# Grab the WCS information
wcs = WCS(hdu.header)

# Size of image
hdu.data.shape

fig = plt.figure()
fig.add_subplot(111, projection=wcs)  # may require WCSAxes http://wcsaxes.readthedocs.org
plt.imshow(hdu.data, origin='lower', cmap='cubehelix')
plt.xlabel('RA')
plt.ylabel('Dec')
plt.show()

# Export header to pickle, just for fun
import pickle
header = hdu.header
pickle.dump(header, open('header.pkl','w'))
# Can then load with pickle.load(open('header.pkl','r'))

