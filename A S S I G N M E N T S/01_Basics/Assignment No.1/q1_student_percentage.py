#Write a program to calculate the percentage of student based on marks of any 5 subjects

#Take an input as marks of 5 subjects 
maths= int(input("Enter marks of subject1:"))
sci= int(input("Enter marks of subject2:"))
geo= int(input("Enter marrk of subject3:"))
his= int(input("Enter marks of subject4:"))
eng= int(input("Enter marks of subject5:"))

#Perform operations
gain_marks= maths + sci + geo + his + eng
percentage= (gain_marks / 500) * 100

#Display the result
print(f"Percentage is {percentage}%")