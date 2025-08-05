#!/usr/bin/python3

def div_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    test_numbers = [10, 25, 30, 45, 100]
    for number in test_numbers:
        if div_by_ten(number):
            print(f"{number} is divisible by 10.")
        else:
            print(f"{number} is not divisible by 10.")