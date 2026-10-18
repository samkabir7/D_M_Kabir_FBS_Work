# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and default)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0

    def __init__(self, bid=None, bname=None, price=None, author=None):
        Book.count += 1
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Destructor is called.")

    def ShowBook(self):
        print('ID:', self.bid)
        print('NAME', self.bname)
        print('PRICE:', self.price)
        print('AUTHOR:', self.author)
        print('##################################')

    @staticmethod
    def totalBooks():
        return Book.count

b1 = Book(101)
b2 = Book(102, 'Atomic Habits', 250, 'James Clear' )
b3 = Book(103, 'Zero to One', 290, 'Peter Theil')

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

print('Total Books:', Book.totalBooks())

