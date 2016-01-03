#!/usr/bin/python
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


FILENAME = "./data/HB101-N2-before-worm1_to_15.dat"


# read data from a text file. One number per line
def get_data_list(filename):
    """ 
    @filename: filename string
    return: a list contains the data

    read a file with data which is one-value-per-line and
    store/return the value as a list.
    """
    data_list = []
    for item in open(filename, 'r'):
        item = item.strip()
        if item != '': 
            try:
                data_list.append(float(item))
            except ValueError:
                pass
    return data_list


# best fit of data
data_list = get_data_list(FILENAME)
(mu, sigma) = norm.fit(data_list)

# the histogram of the data
n, bins, patches = plt.hist(data_list, 60, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

#plot
plt.xlabel('Speed')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ Bug\ Speed:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)

plt.show()
