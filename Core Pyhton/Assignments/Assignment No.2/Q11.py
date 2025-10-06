# Write a program to accept an interger amount from user and tell minimum number of notes needed for representing that amount.

int= int(input("Enter the value of amount:"))

amount= int
d1= amount // 2000
amount= amount % 2000
d2= amount // 500
amount= amount % 500
d3= amount // 200
amount= amount % 200
d4= amount // 100
amount= amount %100
d5= amount // 50
amount= amount % 50
d6= amount // 20
amount= amount %20
d7= amount // 10
amount= amount % 10

sum= d1 + d2 + d3 + d4 + d5 + d6 + d7

print(f"minimum no. of notes to representing amount {int} is {sum}.")
