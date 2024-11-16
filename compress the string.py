from itertools import groupby

# Read the input string
s = input()

# Use groupby to group consecutive characters
result = [(len(list(group)), key)for key, group in groupby(s)]

# Format the result with spaces between tuples
print(" ".join([f"({count}, {char})"for count, char in result]))
