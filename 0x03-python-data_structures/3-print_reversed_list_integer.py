#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None

    reversedList =  list.reverse(my_list)
    if i in reversedList:
        print("{:d}".format(i))
