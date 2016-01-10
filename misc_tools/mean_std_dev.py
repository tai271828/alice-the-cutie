#!/usr/bin/python
import numpy as np
import posixpath

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

if __name__ == '__main__':
    for fileno in range(1, 17):
        filename = "../data/160109/arr" + str(fileno) + "_1.txt"
        data = get_data(filename)
        np_data = np.array(data)
        print "%s: mean: %s std-dev: %s median: %s" % (posixpath.basename(filename), str(np_data.mean()), str(np_data.std()), str(np.median(np_data)))
