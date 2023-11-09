#class vs. Instance variables 
class Rectangle():
    recs =[] #class variable 
    def __init__ (self,width,length):
        self.width = width
        self.length = length
        self.recs.append((self.length, self.width))
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*self.length + 2*self.width 
    def print_size(self):
        print('[] by []'.format(self.length, self.width))
    
r1 = Rectangle(20,25)
print(r1.recs)

class Dog():
    species = 'mammal'
    def __init__ (self,name,age):
        self.name = name
        self.age = age 
Max = Dog('Max', 3)
print(Max.species)


    





