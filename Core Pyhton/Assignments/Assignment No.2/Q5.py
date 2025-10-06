# Write a program to calculate selling price of book based on cost price & discount

cost_price= int(input("Enter a cost price of book:"))
discount= float(input("Enter a discount of book (in %):"))

discount_value= (discount*cost_price)/100

sell_price= cost_price - discount_value

print(f"Selling price of book having cost price is {cost_price} & discount is {discount}% is {sell_price}.")