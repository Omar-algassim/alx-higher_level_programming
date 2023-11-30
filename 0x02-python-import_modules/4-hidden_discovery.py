#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)
    length = len(hidden)
    for i in range(0, length):
        if hidden[i][0] != '_':
            print(hidden[i])
