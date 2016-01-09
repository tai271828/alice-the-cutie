import time
import plotly.plotly as py
import plotly.graph_objs as go

THRESHOLD = 80

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


def get_trace_2(filename):
    data = get_data(filename)
    trace = go.Box(
        x=data,
        name=filename,
        boxpoints='suspectedoutliers',
        marker=dict(
            color='rgb(8, 81, 156)',
            outliercolor='rgba(219, 64, 82, 0.6)',
            line=dict(
                outliercolor='rgba(219, 64, 82, 1.0)',
                outlierwidth=2
            )
        ),
        boxmean='sd'
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


for fileno in range(1, 17, 2):
    filename1 = "../data/160109/arr" + str(fileno) + "_1.txt"
    filename2 = "../data/160109/arr" + str(fileno + 1) + "_1.txt"
    data = [get_trace_2(filename1), get_trace_2(filename2)]
    layout = None
    fig = None
    if THRESHOLD:
        layout = go.Layout(xaxis=dict(range=[0, 100]))
    if layout:
        fig = go.Figure(data=data, layout=layout)
    else:
        fig = go.Figure(data=data)
    plot_url = py.plot(fig, filename="160109-box-3-threshold-80/" + str(fileno))
