## WAP to print sum of series upto n.

n= int(input("ENter the number till you want to get series: "))

i=1
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print(f"Sum of series is {sum}")
