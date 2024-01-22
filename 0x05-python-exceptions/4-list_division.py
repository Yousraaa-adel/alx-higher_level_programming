#!/usr/bin/python3
"""
    This is the "3-safe_print_division" module

    The 3-safe_print_division module supplies one function.
"""


def list_division(my_list_1, my_list_2, list_length):
    div = []
    tmp_result = 0

    for i in range(0, list_length):
        try:
            my_list_1[i] / my_list_2[i]
        except TypeError:
            tmp_result = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp_result = 0
            print("division by 0")
        except IndexError:
            tmp_result = 0
            print("out of range")
        finally:
            div.append(tmp_result)

    return div
