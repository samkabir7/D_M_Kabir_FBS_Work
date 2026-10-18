# WAP to print factorial of a number .
n= int(input("Enter the number want to get its factorial: "))

i=1
fact=1
while(i<=n):
    fact= fact * i
    i+=1
print(f"Factorial of given number {n} is {fact}")


###Using FOR LOOP
n= int(input("ENter number: "))
fact=1
for i in range(1,n+1):
    fact= fact*i
print(fact)