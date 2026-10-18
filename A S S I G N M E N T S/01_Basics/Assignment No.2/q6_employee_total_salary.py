# Write a program to calculate a total salary of an employee based on basic, da=10% on basic, ta=12% on basic, hra=15% on basic.

basic= int(input("Enter the basic pay of employee:"))

# da= int(input("Enter the da of basic pay:"))

# ta= int(input("Enter the ta of basic pay:"))

# hra= int(input("Enter the hra of basic pay:"))

da_pay= basic*(10/100) # here hardcoded values are given so no need to get input for da and ta
ta_pay= basic*(12/100)
hra_pay= basic*(15/100)

total_salary= basic + da_pay + ta_pay + hra_pay

print(f"Total salary of employee having da is{da_pay}, ta is {ta_pay} & hra is {hra_pay} is {total_salary}.")
