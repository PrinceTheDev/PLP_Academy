#!/usr/bin/python3

"""This module provides a simple calculator with basic operations."""


print("Welcome to PLP calculator")
print("Please input two numbers and an operator (+, -, *, /) below:")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter a single operator(+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero error"
else:
    result = "Invalid operator"
print(f"The result of {num1} {operator} {num2} is: {result}")
print("Thank you for using PLP calculator!")