# Write a program to swap a two numbers using third variable.

x= int(input("Enter value of x:"))
y= int(input("Enter value of y:"))

print(f" before swappping x is {x} & y is {y}.")

z=x #we take another container for swapping
x=y
y=z

print(f" after swapping x is {x} & y is {y}.")