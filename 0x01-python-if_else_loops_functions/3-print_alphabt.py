#!/usr/bin/python3
# Print the alphabet in lowercase, without the letters q and e.
for letter in range(97, 123):
  if letter != ord('q') and letter != ord('e'):
    print(chr(letter), end="")

