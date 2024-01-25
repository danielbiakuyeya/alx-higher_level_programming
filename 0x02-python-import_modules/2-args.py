#!/usr/bin/python3

import sys
if __name__ == "__main__":
    l_len = len(sys.argv) - 1
    if l_len == 0:
        print("0 arguments.")
    elif l_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l_len))
    for i in range(l_len):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
