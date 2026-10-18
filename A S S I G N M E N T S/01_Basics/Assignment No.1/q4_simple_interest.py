#Write a program to enter P, T, R and calculate simple interest

principal= float(input("Enter principal:"))
rate= float(input("Enter rate:"))
time= float  (input("Enter time (in yrs):"))

simple_interest= (principal * rate * time) / 100

print(f"Simple interest is {simple_interest}.")