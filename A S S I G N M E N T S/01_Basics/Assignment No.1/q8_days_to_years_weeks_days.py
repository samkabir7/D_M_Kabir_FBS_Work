# Write a program to convert days into years, week and days 

input_days= int(input("Enter the number of days:"))

yrs= input_days // 365
days= input_days % 365
week= days // 7
required_days= days % 7

print(f"years from days {input_days} is {yrs}.")
print(f" weeks from days {input_days} is {week}.")
print(f" days from days {input_days} is {required_days}")
