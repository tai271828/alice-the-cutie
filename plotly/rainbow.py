from numpy import *
import plotly.plotly as py
import plotly.graph_objs as go
import posixpath

N = 4
THRESHOLD = 80

# generate an array of rainbow colors by fixing the saturation and lightness of the HSL representation of colour 
# and marching around the hue. 
# Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.
c = ['hsl('+str(h)+',50%'+',50%)' for h in linspace(0, 360, N)]

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


def get_trace_0(filename):
    data = get_data(filename)
    trace = go.Box(
        y=data,
        name='All points',
        jitter=0.3,
        pointpos=-1.8,
        marker=dict(
            color='rgb(7, 40, 89)',
        ),
        boxpoints='all'
    )
    return trace


def get_trace_1(filename):
    data = get_data(filename)
    trace = go.Box(
        y=data,
        name='Only Whiskers',
        marker=dict(
            color='rgb(9, 56, 125)',
        ),
        boxpoints=False
    )
    return trace


def get_trace_2(filename, i):
    data = get_data(filename)
    trace = go.Box(
        y=data,
        name=posixpath.basename(filename).split(".")[0],
        boxpoints='suspectedoutliers',
        marker={'color': c[i]}
    )
    return trace


def get_trace_3(filename):
    data = get_data(filename)
    trace = go.Box(
        x=data,
        name='Whiskers & Outliers',
        marker=dict(
            color='rgb(107, 174, 214)',
        ),
        boxpoints='Outliers',
        boxmean='sd'
    )
    return trace

trace_list = []

for batch in [1,3,5,7]:
    for fileno in [batch, batch+1, batch+8, batch+9]:
        filename = "../data/160110/arr" + str(fileno) + ".txt"
        if batch == 1:
            trace_list.append(get_trace_2(filename, 0))
        elif batch == 3:
            trace_list.append(get_trace_2(filename, 1))
        elif batch == 5:
            trace_list.append(get_trace_2(filename, 2))
        else:
            trace_list.append(get_trace_2(filename, 3))


    layout = None
    fig = None

    if THRESHOLD:
        layout = go.Layout(yaxis=dict(range=[0, THRESHOLD+20]))
    if layout:
        fig = go.Figure(data=trace_list, layout=layout)
    else:
        fig = go.Figure(data=trace_list)

    plot_url = py.plot(fig, filename="rainbow-160110-4batch/threshold-80", auto_open=False)
