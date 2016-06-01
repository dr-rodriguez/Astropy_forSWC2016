# Generate random numbers and export to a file
import numpy as np
import matplotlib.pyplot as plt

# Examples
# data_x = np.linspace(5000, 8000, 100)  # evenly distributed
# data_x = np.random.randn(100)  # random values from standard normal

# Generate data
np.random.seed(10)  # make reproducible
num = 80
data_x = (np.arange(0, num, 1) - 10) + np.random.randn(num)
a0 = 12.4
a1 = -3.1
a2 = 0.2
noise = 52
data_y = a0 + a1 * data_x + a2 * data_x**2 + noise * np.random.randn(num)

# Examine
plt.plot(data_x, data_y, color='blue', marker='o', linestyle='')
plt.plot(data_x, a0 + a1 * data_x + a2 * data_x**2, color='black', marker='', linestyle='-')

# Mix it up
ind = np.arange(num)
np.random.shuffle(ind)
data_x = data_x[ind]
data_y = data_y[ind]

# Output
data = np.array(zip(data_x,data_y))
with open('text_data.txt','w') as f:
    for x, y in data:
        txt = '{}, {}\n'.format(x,y)
        f.write(txt)
