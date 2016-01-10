#!/usr/bin/python
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import numpy as np
import posixpath
import plotly.graph_objs as go


THRESHOLD = 80


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


def get_trace(filename, fileno):
    data = get_data(filename)
    label = ""
    if fileno % 2 == 1:
        label = posixpath.basename(filename).split(".")[0] + ":before stimulation"
    else:
        label = posixpath.basename(filename).split(".")[0] + ":after stimulation"
    trace = go.Histogram(
        x=data,
        name=label,
        opacity=0.75,
        histnorm='density'
    )
    return trace



for fileno in range(1, 17, 2):
    filename1 = "../data/160110/arr" + str(fileno + 1) + ".txt"
    filename2 = "../data/160110/arr" + str(fileno) + ".txt"
    trace_01 = get_trace(filename1, fileno)
    trace_02 = get_trace(filename2, fileno)

    hist_data = [trace_01, trace_02]

    layout = go.Layout(
        barmode='overlay'
    )

    fig = go.Figure(data=hist_data, layout=layout)

    plot_url = py.plot(fig, filename="160110-histogram-2-threshold-80-density/" + str(fileno), auto_open=False)
