#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def square_matrix_simple(matrix=[]):
  result = []
  new_row = []

  for row in matrix:
    new_row = []
    for value in row:
        new_row.append(value ** 2)
    result.append(new_row)

  return result
