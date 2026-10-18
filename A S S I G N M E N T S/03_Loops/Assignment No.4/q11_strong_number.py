# 11. WAP to check if given number Strong Number.

num = int(input("Enter number: "))

sum = 0
n = num
while(n != 0):
    d = n % 10

    fact = 1
    i =  1
    while(i<=d):
        fact = fact * i
        i += 1

    sum = sum + fact
    n = n // 10

if(sum == num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not strong number")