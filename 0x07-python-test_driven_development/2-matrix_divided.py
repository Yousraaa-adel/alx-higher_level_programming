#!/usr/bin/python3
"""
    This is the "2-matrix_divided" module

    The 2-matrix_divided module divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list of lists): First value
        div (int, float): Second value

    Raises:
        TypeError: If matrix and div are of type int or float
        TypeError: If matrix (list of lists) is not of integers or floats
        TypeError: If matrix rows are not of the same size
        ZeroDivisionError: If div equal zero

    Returns:
        list: A new matrix divided by div, rounded to 2 decimal places
    """

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    
    newMatrix = []

    # Check if all rows have the same size
    row_size = len(matrix[0])

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        newRow = []
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for n in row:
            if (not isinstance(n, int) and not isinstance(n, float)) or isinstance(n, bool):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
            if ( not isinstance(div, int) and not isinstance(div, float)) or isinstance(div, bool):
                raise TypeError("div must be a number")

            if div == 0:
                raise ZeroDivisionError("division by zero")
            
            result = n / div
            newRow.append(round(result, 2))
        newMatrix.append(newRow)
    
    return newMatrix
            