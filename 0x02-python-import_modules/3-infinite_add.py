#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_len = len(sys.argv) - 1

    if args_len == 0:
        print("{}".format(0))
    elif args_len == 1:
        print("{}".format(sys.argv[1]))
    else:
        total_sum = 0
        for i in range(args_len):
            total_sum = total_sum + (int(sys.argv[i + 1]))

        print("{}".format(total_sum))
