#!/usr/bin/python3

# write a program that prints numbers from 0 - 99

for num in range(100):
    if num < 99:
        print("{0:02d}, ".format(num), end="")
        
    else:
        print(num)



