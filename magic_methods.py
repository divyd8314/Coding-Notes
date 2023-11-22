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