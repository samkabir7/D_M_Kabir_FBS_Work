#Write a program to check whether the triangle is equilateral, isosceles or scalene
#triangle.

a= int(input("Enter the side 1: "))
b= int(input("Enter the side 2: "))
c= int(input("Enter the side 3: "))

if(a==b==c):
    print("Traingle is equilateral.")
elif(a==b or b==c or c==a):
    print("Triangle is isosceles.")
else:
    print("Triangle is scalene.")