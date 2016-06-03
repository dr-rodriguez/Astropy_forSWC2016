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
plt.show()

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
plt.show()

# Save results
f = open('results.txt', 'w')
f.write(res)
f.close()
# Examine file: what is wrong?

# Try a different way:
with open('results.txt','w') as f:
    f.write(str(res[:]) + '\n')

# Try yet another way :
f = open('results.txt', 'w')
for i in res:
    f.write(str(i))
    f.write('\n')
f.close()

# Python pickles
import pickle
pickle.dump(res, open('results.pkl', 'w'))
# Can then load with
new_res = pickle.load(open('results.pkl', 'r'))

