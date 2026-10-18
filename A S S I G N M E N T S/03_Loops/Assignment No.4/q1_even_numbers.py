#WAP to print all even numbers until n.

n= int(input("Enter the number till you want to print even number: "))
i=1
while(i<=n):
    if(i%2 ==0):
        print(i)
    i+=1