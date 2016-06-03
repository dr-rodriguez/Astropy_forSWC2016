# Read in data, plot it, fit it
import numpy as np
import matplotlib.pyplot as plt

# Load the data
# See http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
data = np.loadtxt('text_data.txt', delimiter=',')

# Examine data
print(data.shape)
xdata = data[:,0]
ydata = data[:,1]
plt.plot(data[:, 0], data[:, 1], color='blue', marker='o', linestyle='')


# Fit with Numpy
coeff = np.polyfit(data[:, 0], data[:, 1], 2)
print(coeff)  # coefficients of the fit


plt.plot(xdata, coeff[2] + coeff[1] * xdata + coeff[0] * xdata**2, color='red', marker='', linestyle='-')


# Fit with SciPy
# See http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#scipy.optimize.curve_fit
from scipy.optimize import curve_fit

# Write a function for scipy
def myfunction(x, a, b, c):
    return a + b * x + c * x**2

res, cov = curve_fit(myfunction, data[:, 0], data[:, 1])

print(res)  # Best fit parameters
print(cov)  # Covariance of parameters
perr = np.sqrt(np.diag(cov))
print(perr)  # Standard deviation errors from diagonal of covariance matrix

xdata2 = np.sort(data[:, 0])  # for convenience in plotting

plt.plot(data[:, 0], data[:, 1], color='blue', marker='o', linestyle='')
plt.plot(xdata2, myfunction(xdata2, *res), color='green', marker='', linestyle='--', lw=2)


# Save results
f = open('results.txt', 'w')
f.write(res)
f.close()

with open('results.txt','w') as f:
    f.write(str(res[:]) + '\n')
# Examine file: what is wrong?

# Try a diferent way:
f = open('results.txt', 'w')
for i in res:
    f.write(str(i))
    f.write('\n')
f.close()

# Try again:
with open('results2.txt', 'w') as f:
    f.write(' '.join([str(x) for x in res]))

# Python pickles
import pickle
pickle.dump(res, open('results.pkl', 'w'))
# Can then load with
new_res = pickle.load(open('results.pkl', 'r'))

