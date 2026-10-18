#Write a program to calculate profit or loss.

cost_price= int(input("Enter the cost price: "))
sell_price= int(input("Enter the sell price: "))
profit= sell_price - cost_price

if(sell_price > cost_price):
    print("There is a profit.")
    print(f"Profit is {profit}")

else:
    print("There is a loss.")