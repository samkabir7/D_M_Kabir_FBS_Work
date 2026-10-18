#Write a program to find quotient and remainder of two numbers

#take two numbers
num1= int(input("Enter the num1:"))
num2= int(input("Enter the num2:"))

#perform operations
quotient= num1 // num2
remainder= num1 % num2

print(f"Quotient of {num1} & {num2} is {quotient}.")
print(f"Remainder of {num1} & {num2} is {remainder}")