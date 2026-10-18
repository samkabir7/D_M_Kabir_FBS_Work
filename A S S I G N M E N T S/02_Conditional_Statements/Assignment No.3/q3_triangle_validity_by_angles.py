#Write a program to input angles of a triangle and check whether triangle is valid or not.

a= int(input("Enter angle1: "))
b= int(input("Enter angle2: "))
c= int(input("Enter angle3: "))

if(a + b + c == 180 and a>0 and b>0 and c>0 ):
    print("Triangle is valid.")

else:
    print("Triangle is not valid.")