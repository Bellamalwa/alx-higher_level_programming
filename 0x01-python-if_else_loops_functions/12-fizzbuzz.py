#!/usr/bin/python3
# Print the numbers from 1 to 100, separated by a space.
# For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz" instead of the number.
# For multiples of three and five, print "FizzBuzz" instead of the number.
def fizzbuzz():
  for number in range(1, 101):
    fizzbuzz_output = ""
    if number % 3 == 0:
      fizzbuzz_output += "Fizz"
    if number % 5 == 0:
      fizzbuzz_output += "Buzz"
    if fizzbuzz_output:
      print(fizzbuzz_output, end=" ")
    else:
      print(number, end=" ")

fizzbuzz()
