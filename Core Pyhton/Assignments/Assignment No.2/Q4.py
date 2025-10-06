#Write a program to calculate area of triangle and rectangle 

#We can interchange the order as well

base= float(input("Enter base of a triangle:"))
height= float(input("Enter height of a triangle:"))

Area_of_triangle= 1/2 * (base*height)         

print(f"Area of triangle is {Area_of_triangle}.")

length= float(input("Enter length of rectangle:"))
breadth= float(input("Enter breadth of rectangle:"))

Area_of_rectangle= length*breadth

print(f"Area of rectangle is {Area_of_rectangle}.")