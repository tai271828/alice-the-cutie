#!/usr/bin/python

FILENAME="arr1new.txt"

def matrix2column(filename):
    """
    @filename: a file contains data format looks like
        <string1: value01, value02, .....>
        <string2: value11, value12, .....>
    return: a list looks like
        [value01, value11, ......, value02, value12......]
    """
    data_list = []
    for item in open(filename, 'r'):
        item = item.strip()
        item = item.split('\t')
        if item != '':
            try:
                for element in item:
                    data_list.append(float(element))
            except ValueError:
                pass
    return data_list


if __name__ == '__main__':
    file_2_write = open(FILENAME + ".matrix2column", 'w')
    data_list = matrix2column(FILENAME)
    for item in data_list:
        file_2_write.write(str(item)+"\n")
