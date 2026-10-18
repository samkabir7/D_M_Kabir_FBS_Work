# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        cm = self.cm + other.cm
        m = cm // 100
        cm = cm % 100

        m= m + self.m + other.m
        km = m // 1000
        m = m % 1000

        km = km + self.km + other.km

        return f'{km} : {m} : {cm}'
    

    def __sub__(self, other):      #to perform substractioin you must do whole distance in cm cause it is the lowest in distance
        total_cm1 = self.km*100000 + self.m*100 + self.cm
        total_cm2 = other.km*100000 + other.m*100 +other.cm

        diff_cm = abs(total_cm1 - total_cm2)                 #abs() >> used to avoid negative dist values , it returns absolute value

        km = diff_cm // 100000
        diff_cm = diff_cm % 100000
        m = diff_cm // 100
        cm = diff_cm % 100

        return f'{km} : {m} : {cm}'
        


d1 = Distance(3, 860, 750)
d2 = Distance(1, 250, 700)
print(d1 + d2)
print(d1 - d2)