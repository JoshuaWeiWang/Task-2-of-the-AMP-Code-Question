#!/bin/python3
import re

if __name__ == '__main__':
    # This is my answer of the task 2 in the AMP Code Question. 
    # Please run this program by the following command:
    # python task2.py
    
    # Enter the values of N and M, respectively
    first_multiple_input = input('Please enter the values of N and M: ').rstrip().split() 
    N = int(first_multiple_input[0])
    M = int(first_multiple_input[1])

    # Initialize the input matrix
    matrix = []

    for row in range(N):
        matrix_item = input('Please enter the items in No. {row} row: '
                            .format(row = row + 1))
        matrix.append(matrix_item)

    # Decode the matrix script as output
    output = "".join([row[item] for item in range(M) for row in matrix])

    output = re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', output)
    output = re.sub('  ', ' ', output)
    
    # Print the output of this program
    print(output)