#Write a program to input two angles from user and find third angle of the triangle

angle1= int(input("Enter angle1:"))
angle2= int(input("Enter angle2:"))

third_angle= 180 - ( angle1 + angle2 )

print(f"third angle of triangle is {third_angle}.")