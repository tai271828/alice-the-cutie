#!/usr/bin/python
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# read data from a text file. One number per line
arch = "./data/HB101-N2-before-worm1_to_15.dat"
datos = []
for item in open(arch,'r'):
    item = item.strip()
    if item != '':
        try:
            datos.append(float(item))
        except ValueError:
            pass

# best fit of data
(mu, sigma) = norm.fit(datos)

# the histogram of the data
n, bins, patches = plt.hist(datos, 60, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

#plot
plt.xlabel('Speed')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ Bug\ Speed:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)

plt.show()
