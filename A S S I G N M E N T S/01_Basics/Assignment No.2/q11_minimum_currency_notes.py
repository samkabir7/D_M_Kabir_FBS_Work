# Write a program to accept an interger amount from user and tell minimum number of notes needed for representing that amount.

int= int(input("Enter the value of amount:"))

amount= int
N1= amount // 2000
amount= amount % 2000
N2= amount // 500
amount= amount % 500
N3= amount // 200
amount= amount % 200
N4= amount // 100
amount= amount %100
N5= amount // 50
amount= amount % 50
N6= amount // 20
amount= amount %20
N7= amount // 10
amount= amount % 10

sum= N1 + N2 + N3 + N4 + N5 + N6 + N7

print(f"minimum no. of notes to representing amount {int} is {sum}.")
