#!/usr/bin/python3

list = input("Enter a list of numbers seperated by a comma for addition: \n")
list = list.split(",")
default = 0

for i in list:
    default += int(i)

print(f"The current sum is {default}")