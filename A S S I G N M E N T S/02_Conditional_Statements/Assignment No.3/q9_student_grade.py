#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1= int(input("Enter the marks of 1st subject: "))
m2= int(input("Enter the marks of 2nd subject: "))
m3= int(input("Enter the marks of 3rd subject: "))
m4= int(input("Enter the marks of 4th subject: "))
m5= int(input("Enter the marks of 5th subject: "))

sum= m1 + m2 + m3 + m4 + m5
print("sum:", sum)

if(sum>460):
    print("This is first class.")
elif(sum>440):
    print("This is second class.")
elif(sum>420):
    print("This is third class.")
elif(sum>400):
    print("This is fourth class.")
elif(sum>350):
    print("This is fifth class.")
else:
    print("Gained marks not in grades.")