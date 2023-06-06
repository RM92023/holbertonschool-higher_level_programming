#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in range(len(my_list)-1, -1, -1):
        if isinstance(my_list[i], int):
            print('{}'.format(my_list[i]))
