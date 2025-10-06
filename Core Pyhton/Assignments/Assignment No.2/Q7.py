# Find the sum of three digit number

three_digit_number= int(input("Enter three digit numbers:"))

num= three_digit_number
d1= num % 10           #it gives unary number (remainder)
num= num // 10         #it gives remaining numbers (quotient)
d2= num % 10
num= num // 10
d3= num % 10          # when it gets zero stop this process
num= num // 10

sum= d1 + d2 + d3

print(f"Sum of three digit number is {three_digit_number} is {sum}.")