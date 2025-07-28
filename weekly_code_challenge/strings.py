#!/usr/bin/python3


list_of_words = ["apple", "banana", "cherry", "date", "elderberry"]

odd_words = [word for word in list_of_words if len(word) % 2 != 0]
print(f"Words with odd lengths: {odd_words}")