#!/usr/bin/python
import plotly.plotly as py
from plotly.tools import FigureFactory as FF

import numpy as np
# read data from a text file. One number per line
def get_data_list(filename):
    arch = filename
    datos = []
    for item in open(arch,'r'):
        item = item.strip()
        if item != '':
            try:
                datos.append(float(item))
            except ValueError:
                pass
    return datos
data_01 = get_data_list("alice-is-cute-HB101afterN2.txt")
data_02 = get_data_list("alice-is-cute-HB101afterN2-02.txt")

hist_data = [data_01, data_02]

group_labels = ['Group 1', 'Group 2']

colors = ['rgb(0, 0, 100)', 'rgb(300, 200, 200)']

# Create distplot with curve_type set to 'normal'
fig = FF.create_distplot(hist_data, group_labels, bin_size=.5, curve_type='normal', colors=['rgb(0, 0, 100)', 'rgb(0, 200, 200)'])

# Add title
fig['layout'].update(title='Alice is so cute so I plot this for her!!!')

# Plot!
py.iplot(fig, filename='two-cute-plots-and-sleepy', validate=False)
