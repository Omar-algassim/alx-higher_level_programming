#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print("")
        return i + 1
    except IndexError:
        print("")
        return i + 1
    except (TypeError, ValueError):
        pass
    