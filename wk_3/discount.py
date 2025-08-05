#!/usr/bin/python3

def calculate_discount(price, discount_percent):
    if discount_percent <= 0.2:
        return price
    else:
        discount_amount = price * discount_percent
        price = price - discount_amount
        return price
    
def main():
    input_price = float(input('Enter the price:'))
    input_discount = float(input('Enter the discount percentage:')) / 100

    final_price = calculate_discount(input_price, input_discount)
    print(f'The final price after discount is: {final_price:.2f}')

    if input_discount < 0.2:
        print(f'{input_price:.2f}')

if __name__ == "__main__":
    main()
    