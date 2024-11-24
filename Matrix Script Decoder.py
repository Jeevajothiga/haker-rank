"""Problem Description:
In this problem, you are given a 2D matrix represented by n rows and m columns, where each cell contains a string of alphanumeric characters, spaces, and special symbols. The goal is to decode the matrix by reading its columns top to bottom, and transforming the resulting characters to create a readable sentence.

Transformation Rules:
Each string's first character remains unchanged.
For each subsequent character in the string, if a non-alphanumeric character (such as spaces or symbols) appears between two alphanumeric characters, it should be replaced with a single space.
The final output should be the transformed sentence where symbols/spaces between alphanumeric characters are replaced with a single space.
Input:
Two integers n and m representing the number of rows and columns of the matrix.
n strings of length m, each containing alphanumeric characters, spaces, and special symbols.
Output:
A single string representing the decoded matrix where unwanted symbols and spaces between alphanumeric characters are replaced by a single space.
Constraints:
1 ≤ n, m ≤ 500
The matrix contains only upper and lower case English letters, numbers, spaces, and symbols (!, @, #, $, %, &)."""
import math
import os
import random
import re
import sys

# Read the dimensions of the matrix
n, m = map(int, input().split())

# Read the matrix rows
matrix = [input() for _ in range(n)]

# Initialize an empty string to store the decoded script
decoded_script = ""

# Loop through each column
for col in range(m):
    # For each column, we read characters from top to bottom
    for row in range(n):
        decoded_script += matrix[row][col]

# Use regex to replace symbols/spaces between alphanumeric characters with a single space
# This pattern matches non-alphanumeric characters that are between alphanumeric ones and replaces them with a space
decoded_script = re.sub(r'(?<=\w)[^A-Za-z0-9]+(?=\w)', ' ', decoded_script)

# Print the final decoded script
print(decoded_script)




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
