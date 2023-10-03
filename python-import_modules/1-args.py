#!/usr/bin/python3

def print_arg(argv):

    length = len(argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
        return
    else:
        if length == 1:
            print("{} argument:".format(length))
        else:
            print("{} arguments:".format(length))
        n = 1
        while n <= length:
            print("{}: {}".format(n, argv[n]))
            n += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)