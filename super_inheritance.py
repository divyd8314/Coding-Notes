class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*self.length+2*self.width
    
    def what_am_I(self):
        return 'Rectangle'

class Square(Rectangle):
    def __init__ (self,length):
        super().__init__(length,length)
    
    def what_am_I(self):
        return 'Square'

class Cube(Square):
    
    #Same parameters as class square, no need to redefine 
    def surface_area(self):
        face_area = self.area()
        return face_area*6
    
    def what_am_I(self):
        return 'Cube'
    
    def family_tree(self):
        return self.what_am_I() + ' child of ' + super().what_am_I()

cube1 = Cube(3)
print(cube1.surface_area())
print(cube1.family_tree())