#!/usr/bin/python
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import numpy as np
import posixpath


THRESHOLD = 45


# read data from a text file. One number per line
def rm_bad_data(data, threshold):
    rtn_data = []
    for item in data:
        if item < threshold:
            rtn_data.append(item)
    return rtn_data


def get_data(filename):
    data = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line.strip()
        try:
            if line != '':
                data.append(float(line))
        except ValueError:
            pass
    if THRESHOLD:
        data = rm_bad_data(data, THRESHOLD)
    return data


for fileno in range(1, 17, 2):
    filename1 = "../data/160109/arr" + str(fileno) + "_1.txt"
    filename2 = "../data/160109/arr" + str(fileno + 1) + "_1.txt"
    data_01 = get_data(filename1)
    data_02 = get_data(filename2)

    hist_data = [data_01, data_02]

    group_labels = [posixpath.basename(filename1), posixpath.basename(filename2)]

    colors = ['rgb(0, 0, 100)', 'rgb(300, 200, 200)']

    # Create distplot with curve_type set to 'normal'
    fig = FF.create_distplot(hist_data, group_labels, bin_size=.5, curve_type='normal', colors=['rgb(0, 0, 100)', 'rgb(0, 200, 200)'])

    # Add title
    #fig['layout'].update(title='Alice is so cute so I plot this for her!!!')

    # Plot!
    py.iplot(fig, filename="160109-histogram-1/" + str(fileno), validate=False)

