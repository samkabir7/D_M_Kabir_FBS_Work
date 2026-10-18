# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and default)
# b. Destructor
# c. ShowBook


class Book:
    def __init__(self, bid=1, bname= 'Atomic Habits', price= 250, author='James Clear'):
        self.bid= bid
        self.bname= bname
        self.price= price
        self.author= author
        
    def getData(self):
        print('ID:', self.bid)
        print('NAME:', self.bname)
        print('PRICE:', self.price)
        print('AUTHOR:', self.author)
        print('######################################')

    def __del__(self):
        print('Destructor is called')


b1= Book()
b1.getData()

b2= Book(2, 'Zero to One', 300, 'Peter Theil')
b2.getData()
