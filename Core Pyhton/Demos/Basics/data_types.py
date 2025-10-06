####DATA TYPES OF PYTHON

#int data type
var=2025
print(type(var))

#float data type
var=3.76
print(type(var))

#complex data type
var=10+3j
print(type(var))

#text data type
var="First Bit Solutions @123" # we can use single inverted comma 
print(type(var))
var1="""" My name is Samarth Kabir  
I am from Nanded"""          # for multiline string we can use triple single or double inverted commas 
#this is not used for the comments       
print(type(var))

#sequential data type
#1. list

var=[10,20,30,40,50]
print(type(var))
print(var)

#2.tuple
var=(10,20,30,40,50)
print(type(var))
print(var)

#### set type
#1.Set

var={10,20,30,40}
print(type(var))
print(var)

#2. frozenSet

var={10,20,30,40}
print(type(var))
print(var)


#### mapping
#1.dict

var={'id':101, 'name':'Sam Kabir'}
print(type(var))
print(var)

#### Boolean 
#1. True
var=True # always take capital letters
print(type(var))
print(var)

#2. False # always take capital letters
var=False
print(type(var))
print(var)

#### None

var=None # always take capital letters
print(type(var))
print(var)


#text (range)
var= range(12)
print(type(var))
print(list(var))

