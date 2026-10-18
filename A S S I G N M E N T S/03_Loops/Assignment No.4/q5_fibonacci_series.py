# 5. WAP to print Fibonacci series upto n.

n = int(input("Enter number: "))

a = 0
b = 1

while(a<=n):
    print(a)
    c = a + b
    a = b
    b = c


# agr n terms chahiye to for loop use hoga for i in range(n):