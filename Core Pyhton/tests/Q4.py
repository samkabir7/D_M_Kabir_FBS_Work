length= float(input("Enter the lenght of wall:"))
breadth= float(input("Enter the breadth of wall:"))

area_of_one_wall= length * breadth
area_of_interior= length * breadth
area_of_exterior= length * breadth

print(f"Area of one wall : {area_of_one_wall}.")
print(f"Area of interior: {area_of_exterior}.")
print(f"Area of exterior : {area_of_interior}.")

cost_of_interior= int(input("Enter the cost of interior:"))
cost_of_exterior= int(input("Enter the cose of exterior:"))

cost_of_painting= cost_of_interior + cost_of_exterior + (area_of_one_wall * 8)

print(f"Cost of painting for all buildings wall is {cost_of_painting}.")



