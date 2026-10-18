## WAP to check if a given number is prime number or not.

n= int(input("ENter number to check prime or not: "))

for i in range(2,n+1):
    if(n%i==0):
        print(f"{n} is not a prime number.")
        break ## to stop the execution of loop

else:
    print(f"{n} is a prime number")

# 6. WAP to check if a given number is prime number or not.

n = int(input("Enter number: "))

i = 2
while(i<n):
    if(n % i == 0):
        print(f"{n} is not prime number")
        break
    i +=1

else:
    print(f"{n} is prime number")