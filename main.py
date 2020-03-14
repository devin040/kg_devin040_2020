import sys
from itertools import zip_longest

"""
Takes two strings and determines if there's a one to one map from string 1 to string 2

@:param str1 first string
@:param str2 second string

@:return 0 if mapping exists; prints true
         1 if no mapping exists; prints false
"""


def str_map(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    map_dict = {}
    for x, y in zip_longest(str1, str2):
        if map_dict.get(x, -1) == -1:
            map_dict[x] = y
        if x in map_dict.keys() and y is None:
            continue
        elif map_dict[x] != y:
            print("false")
            return 1
    if None in map_dict.values():
        print("false")
        return 1
    print('true')
    return 0


if __name__ == "__main__":
    str_map(sys.argv[1], sys.argv[2])
