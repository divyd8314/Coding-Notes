class Person():

    def __init__(self,name):
        self.name=name
    
    def __rep__(self):
        return self.name 

joe = Person('joe')
print(joe)

class Car():

    def __init__(self,colour,mileage):
        self.colour = colour
        self.mileage = mileage 
    def __repr__(self):
        return '{self.__class__.__name__} ({}, x, {})'.format(self.colour, self.mileage, self=self)
    
car1 = Car('blue', 300000)
print(car1)

class AlwaysPositive:

    def __init__(self,number):
        self.n = number
    
    def __add__(self,other):
        return abs(self.n + other.n)
x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x+y)
#by affecting the __add_ method 
#(-20+10)=-10, abs(-10) = 10
#Therefore, 10 is the output 

#Another example
class Basket():
    def __init__(self,contents):
        self.contents = contents 
    
    def __add__ (self,other):
        return Basket(self.contents + other.contents)

mybasket = input("Enter basket items seperated by comma").split(',')
basket = Basket (mybasket)