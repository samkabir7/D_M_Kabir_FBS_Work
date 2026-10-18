# Swapping two numbers in a simple way

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print(f"Before swapping: x = {x}, y = {y}")

x, y = y, x

print(f"After swapping: x = {x}, y = {y}")
