#!/usr/bin/python3

# Write a program that prints all possible different combinations of two digits

def print_two_digits():
  for i in range(10):
    for j in range(i + 1, 10):
      if i != j:
        print(", {:02d}".format(10 * i + j), end="")

print_two_digits()