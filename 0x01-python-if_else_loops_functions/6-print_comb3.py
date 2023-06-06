#!/usr/bin/python3
# Print all possible different combinations of two digits in ascending order, where the two digits are not the same.
# The combination 89 is printed as a single line.
for digit1 in range(0, 10):
  for digit2 in range(digit1 + 1, 10):
    if digit1 != digit2 and digit1 != 8 and digit2 != 9:
      print(digit1, digit2, end=", ")
    elif digit1 == 8 and digit2 == 9:
      print(digit1, digit2)

