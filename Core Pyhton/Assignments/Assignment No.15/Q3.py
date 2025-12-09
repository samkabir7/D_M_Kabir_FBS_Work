# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and default)
# h. Destructor
# i. ShowBook


class Shirt:
    def __init__(self, sid=1, name='Formal shirt', type='formal', price='884', size='L'):
        self.sid= sid
        self.sname= name
        self.type= type
        self.price= price
        self.size= size

    def getData(self):
        data= f'ID:{self.sid}\nNAME:{self.sname}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}'

        return data
    
    def __del__(self):
        print('Destructor is called')
    
s1= Shirt()
print(s1.getData())

print('#################################')
s2= Shirt(2, 'Polo Tshirt', 'Casual', 789, 'M')
print(s2.getData())

        