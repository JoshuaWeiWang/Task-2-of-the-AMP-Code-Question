import re

# Enter the values of N and M, respectively
N = int(input('Please enter the value of N: ').strip().split()[0])
M = int(input('Please enter the value of M: ').strip().split()[0])


# Initialize the input matrix
matrix = []

for row in range(N):
    matrix.append(input('Please enter the items in No. {row} row: '
                        .format(row = row + 1)))

# decode the matrix script as output
output = "".join([row[item] for item in range(M) for row in matrix])

print('The decoded script is: {output}'.format(output = output))

output = re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', output)
output = re.sub(r'[0-9]', '', output)
output = re.sub('  ', ' ', output)

print('The final decoded script is: {output}'.format(output = output))