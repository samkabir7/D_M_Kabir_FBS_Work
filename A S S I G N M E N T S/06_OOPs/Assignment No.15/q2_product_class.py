# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and default)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self, pid=None, pname='', price= None, quantity=0):
        self.pid= pid
        self.pname= pname
        self.price= price
        self.quantity= quantity

    def getData(self):
        data= 'ID:'+str(self.pid)+'\n'
        data+= 'NAME:'+self.pname+'\n'
        data+= 'PRICE:'+str(self.price)+'\n'
        data+= 'QUANTITY:'+str(self.quantity)+'\n'
        data+= '#########################################'

        return data 
    
    def __del__(self):
        print("Destructor Called.")
    
p1= Product()
print(p1.getData())

p2= Product(102, 'Laptop', 67000, 4)
print(p2.getData())
