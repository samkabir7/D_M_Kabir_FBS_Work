#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)

male_age= int(input("Enter age of men: ")) 
female_age= int(input("Enter age of women: "))

if(male_age>=21 and female_age>=18):
    print("person is eligible to marry.")

else:
    print("person is not eligible to marry.")