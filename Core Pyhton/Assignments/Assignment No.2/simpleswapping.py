#Swapping of two numbers in simple way

x= int(input("Enter the value of x:"))
y= int(input("Enter the value of y:"))

print(f"before swappping x is {x} & y is {y}.")

x,y = y,x

print(f"After swappping x is {x} & y is {y}.")