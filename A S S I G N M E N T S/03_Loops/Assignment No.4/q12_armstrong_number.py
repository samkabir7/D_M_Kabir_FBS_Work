# 12. Write a program to check if given number is Armstrong number or not. 
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 
# 4*4*4*4)

num = input("ENter number: ")
count = len(num)

number= int(num)
sum = 0
n = number
while(n != 0):
    d = n % 10
    d = d ** count
    sum = sum + d
    n = n // 10

if(sum == number):
    print("Armstrong")
else:
    print("not")