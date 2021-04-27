#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if i != ord('q') and i != ord('e'):
        print("{0:c}".format(i), end = "")
