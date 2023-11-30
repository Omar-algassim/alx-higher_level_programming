#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    l = len(sys.argv)
    for i in range(1, l):
        result = result + int(sys.argv[i])
    print(result)
