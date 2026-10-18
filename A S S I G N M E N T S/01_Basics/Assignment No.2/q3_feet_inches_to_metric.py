# Convert distance given in feet & inches into meters and centimeters

feet= float(input(" Enter distance in feet:"))
inches= float(input("Enter distance in inches:"))

meters= (feet*0.3048) + (inches*0.0254)
centimeters= (feet*30.48) + (inches*2.54)

print(f"Distance given in {feet} feet & {inches} inches is {meters} meters & {centimeters} centimeters.")