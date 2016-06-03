# A couple of exercizes with FITS files
# From http://www.astropy.org/astropy-tutorials/FITS-images.html
# Written by Lia Corrales

import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits
from matplotlib.colors import LogNorm

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open(image_file)

hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))

print(image_data.shape)

hdu_list.close()
# image_data = fits.getdata(image_file)  # Faster way if you don't need to examine header

plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

#print(type(image_data.flat))
flat_image = image_data.flatten()
NBINS = 1000
histogram = plt.hist(image_data.flatten(), NBINS)
plt.show()

plt.imshow(image_data, cmap='gray', norm=LogNorm())
plt.savefig('horsehead.png')

# Image Stacking
image_list = [download_file('http://data.astropy.org/tutorials/FITS-images/M13_blue_000' + n + '.fits', cache=True) \
              for n in ['1', '2', '3', '4', '5']]

# The long way
image_concat = []
for image in image_list:
    image_concat.append(fits.getdata(image))

final_image = np.zeros(shape=image_concat[0].shape)

for image in image_concat:
    final_image += image  #  This is the same as final_image = final_image + image

plt.hist(final_image.flatten(), 1000)

plt.imshow(final_image, cmap='gray', vmin=2.e3, vmax=3.e3)
plt.colorbar()
plt.show()

# Write to file
outfile = 'stacked_M13_blue.fits'
hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, clobber=True)
