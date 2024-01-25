#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return (0)
    weighted_average = 0
    div = 0
    for data in my_list:
        weighted_average += (data[0] * data[1])
        div += data[1]
    return (weighted_average / div)
