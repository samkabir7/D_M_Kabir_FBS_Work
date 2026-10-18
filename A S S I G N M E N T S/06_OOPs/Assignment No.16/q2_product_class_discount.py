# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and default)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 0.0

    def __init__(self, pid=None, pname="", price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print('Destructor is called.')

    def ShowBook(self):
        print('ID:', self.pid)
        print('NAME:', self.pname)
        print('PRICE:', self.price)
        print('QUANTITY:', self.quantity)
        print('############################################')

    
    def applyDiscount(self):
        discount_price = self.price - (self.price*Product.discount/100)
        return discount_price


    discount = 10 

# p1 = Product(101)
p2 = Product(102, 'Shirt', 780, 4)
p3 = Product(103, 'Pant', 1500, 2)

# p1.ShowBook()
p2.ShowBook()
p3.ShowBook()

print('Price after Discount:', p2.applyDiscount())

print('Price after Discount:', p3.applyDiscount())
