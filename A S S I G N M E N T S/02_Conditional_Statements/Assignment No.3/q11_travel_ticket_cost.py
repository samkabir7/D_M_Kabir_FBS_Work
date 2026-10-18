age1 = int(input("Enter age of person 1: "))
ticket1 = int(input("Enter ticket price: "))

if(age1<12):
   ticket1 = ticket1 - (ticket1*0.30)
elif(age1>59):
   ticket1 = ticket1 - (ticket1*0.50)
else:
   ticekt1 = ticket1

age2 = int(input("Enter age of person 2: "))
ticket2 = int(input("Enter ticket price"))

if(age2<12):
   ticket2 = ticket2 - ( ticket2 * 0.30)
elif(age2>59):
   ticket2 = ticket2 - (ticket2 * 0.50)
else:
   ticket2 = ticket2

age3 = int(input("Enter age of person 3: "))
ticket3 = int(input("Enter ticket price"))

if(age3<12):
   ticket3 = ticket3 - ( ticket3 * 0.30)
elif(age3>59):
   ticket3 = ticket3 - (ticket3 * 0.50)
else:
   ticket3 = ticket3

age4 = int(input("Enter age of person 4: "))
ticket4 = int(input("Enter ticket price"))

if(age4<12):
   ticket4 = ticket4 - ( ticket4 * 0.30)
elif(age4>59):
   ticket4 = ticket4 - (ticket4 * 0.50)
else:
   ticket4 = ticket4

age5 = int(input("Enter age of person 5: "))
ticket5 = int(input("Enter ticket price"))

if(age5<12):
   ticket5 = ticket5 - ( ticket5 * 0.30)
elif(age5>59):
   ticket5 = ticket5 - (ticket5 * 0.50)
else:
   ticket5 = ticket5

total_price = ticekt1 + ticket2 + ticket3 + ticket4 + ticket5
print(f"Total ticket price is {total_price}")

