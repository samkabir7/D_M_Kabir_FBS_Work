#Write a program to enter P, T, R & calculate Compound Interest

P= float(input("Enter principal:"))
R= float(input("Enter rate:"))
T= float(input("Enter time (in yrs):"))

CI= P * ( 1+ R/100) ** T - P #for raise to T we use exponential operator

print(f" Compound interest of {P}, {R}, & {T} is {CI}.")