#!/usr/bin/python3


greetings = print("Please enter your Name, Age and Favorite Color below: \n")
Name = input('Name: ')
Age = input('Age: ')
Favorite_Color = input('Favorite Color: ')

dict = {
    "Name": Name,
    "Age": Age,
    "Favorite Color": Favorite_Color
}

print(f"{dict}")