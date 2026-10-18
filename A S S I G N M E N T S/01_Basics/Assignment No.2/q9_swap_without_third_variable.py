#Swappping of two numbers without third var

x= int(input("Enter the value of x:"))
y= int(input("Enter the value of y:"))

print(f"Before swapping x is {x} & y is {y}.")

x=x*y #if we perform multiplication at first then we have to do division after.
y=x//y
x=x//y

print(f"After swappping x is {x} & y is {y}.")