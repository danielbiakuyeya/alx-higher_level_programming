#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for s in my_string:
        if s != 'c' and s != 'C':
            new_str.append(s)
    return ("".join(new_str))
