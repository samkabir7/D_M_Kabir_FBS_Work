## WAP to check if given number is Perfect Number.

n= int(input("enter number: "))

sum=0
for i in range(1,n):
    if(n%i == 0):
        sum=sum+i

if(sum==n):
    print(f"{n} is a perfect number. ")
else:
    print(f"{n} is not a perfect number.")

# 10. WAP to check if given number is Perfect Number.

n = int(input("Enter number: "))

sum = 0
i = 1
while(i < n):
    if(n % i == 0):
        sum = sum + i
    i += 1

if(sum == n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
