#!/usr/bin/python
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


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


def plot_hist_and_fit_gauss(data_list, binno=60, normed=1, facecolor="green", alpha=0.75, linecolor='r--'):
    """
    return (mu, sigma)
    """
    # fit the data by guass distribution
    # norm.fit returns (mu, sigma)
    (mu, sigma) = norm.fit(data_list)
    # plot the histogram of the data
    (n, bins, patches) = plt.hist(data_list, binno, normed=normed, facecolor=facecolor, alpha=alpha)
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, linecolor, linewidth=2)
    return (mu, sigma)

data_list_1 = get_data_list(FILENAME_1)
mu_sigma_1 = plot_hist_and_fit_gauss(data_list_1, facecolor='cyan', linecolor='g--')

data_list_2 = get_data_list(FILENAME_2)
mu_sigma_2 = plot_hist_and_fit_gauss(data_list_2, facecolor='magenta')

mu_sigma = mu_sigma_1 + mu_sigma_2

#plot
plt.xlabel('Speed')
plt.ylabel('Probability')
plt.title('Histogram of Bug Speed:\nmu1=%.3f, sigma1=%.3f\nmu2=%.3f, sigma2=%.3f' % mu_sigma)
plt.grid(True)

plt.show()
