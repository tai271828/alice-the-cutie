#!/usr/bin/python
import matplotlib.pyplot as plt
from scipy.stats import maxwell
import numpy as np

FILENAME_1 = "./data/HB101-N2-before-worm1_to_15.dat"
FILENAME_2 = "./data/HB101-N2-after-worm1_to_10.dat"


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


def plot_hist_and_fit_gauss(data_list, binno=60, normed=1, facecolor="green", linecolor='r--', alpha=0.5):
    """
    return (mu, sigma)
    """
    # fit the data by maxwell-boltzmann distribution
    # mawell.fit returns shape, loc, scale : tuple of floats
    # MLEs for any shape statistics, followed by those for location and
    # scale.
    params = maxwell.fit(data_list)
    print params
    # plot the histogram of the data
    #(n, bins, patches) = plt.hist(data_list, binno, range=(0, 50), normed=normed, facecolor=facecolor, alpha=alpha)
    (n, bins, patches) = plt.hist(data_list, binno, normed=normed, facecolor=facecolor, alpha=alpha)
    x = np.linspace(0, 25, 100)
    # add a 'best fit' line
    plt.plot(x, maxwell.pdf(x, *params), linecolor, lw=3)
    print get_max_likelihood(data_list, params[0], params[1])
    return params


def get_max_likelihood(data_list, loc, scale, weight=45):
    pdf_array = maxwell.pdf(data_list, loc, scale)
    likelihood = 1
    for item in pdf_array:
        likelihood = item * weight * likelihood
    return likelihood


data_list_1 = get_data_list(FILENAME_1)
params_1 = plot_hist_and_fit_gauss(data_list_1, facecolor='cyan', linecolor='g--', alpha=1)

data_list_2 = get_data_list(FILENAME_2)
params_2 = plot_hist_and_fit_gauss(data_list_2, facecolor='magenta')

#plot
plt.xlabel('Speed')
plt.ylabel('Probability')
plt.title('Histogram of Bug Speed fitted by maxwell-boltzmann distribution:\nbefore=%.3f,after=%.3f' % (params_1[1], params_2[1]))
plt.grid(True)

plt.show()
