# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        realadd = self.real + other.real
        imagadd = self.imag + other.imag

        return f'{realadd} + {imagadd}' 
    
    def __sub__(self, other):
        realsub = self.real - other.real
        imagsub = self.imag - other.imag
        return f'{realsub} + {imagsub}'
    
    def __del__(self):
        print("Destructor is called")

cn1 = ComplexNumber(4 , 5j)          #always use j instead of i in python program
cn2 = ComplexNumber(2 , 1j)
# del cn1 
print(cn1 + cn2)
print(cn1 - cn2)
