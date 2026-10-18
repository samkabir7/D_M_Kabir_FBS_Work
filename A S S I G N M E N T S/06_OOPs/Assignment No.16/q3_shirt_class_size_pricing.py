# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and default)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    size_increment = 0.10

    def __init__(self, sid=None, sname=None, type=None , price=0, size='small'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print('destructor is Called.')

    def ShowBook(self):
        print('ID:', self.sid)
        print('NAME:', self.sname)
        print('TYPE:', self.type)
        print('PRICE:', self.price)
        print('SIZE:', self.size)
        # print('After PRICE:', self.calculatePrice())

    def calculatePrice(self):
        size_order = { 'small':0, 'medium':1, 'large':2, 'xlarge':3 }

        increment_level = size_order.get(self.size, 0)
        final_price =self.price + (self.price * Shirt.size_increment * increment_level)
        return final_price
    
s1 = Shirt(1, 'Peter England', 'formal', 1000, 'large' )
s1.ShowBook()
print('After Price:', s1.calculatePrice())

print('############################################################')
    
s2 = Shirt(1, 'Allen Solly', 'Casual', 1000, 'medium' )
s2.ShowBook()
print('After Price:', s2.calculatePrice())
    


    
