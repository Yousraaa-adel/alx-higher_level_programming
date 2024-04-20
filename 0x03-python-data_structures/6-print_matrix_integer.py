#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for row in matrix:
        for column in row:
            if column == row[-1]:
                print("{:d}".format(column), end="")
            else:
                print("{:d}".format(column), end=" ")
        print()
