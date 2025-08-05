#!/usr/bin/python3

def large_power(base, exponent):
    #calculate base to the power of exponent
    result = base ** exponent

    if result > 5000:
        return True
    else:
        return False



if __name__ == "__main__":
    # Test cases
    print(large_power(10, 3))  # 10^3 = 1000 → False
    print(large_power(10, 4))  # 10^4 = 10000 → True