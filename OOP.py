#Classes and methods 
#Defining a class
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.colour = c
    
    def rot (self, days, temp):
        self.mold = days*temp


#Instantiate an object
orange_1 = Orange(15, 'burnt orange')
orange_2 = Orange(0.8, 'Navel Orange')
orange_3 = Orange(0.6, "blood_orange")
print(orange_1.weight)
print(orange_1.colour)


orange_1.rot(3, 30)
print(orange_1.mold)

#Create a perimeter method, change size method, identify method 
#Instantiate two new rectangles and change their size 
#Run .perimeter on rec1 and .identify on rec2
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def area (self):
        return self.width * self.length 
    def perimeter (self):
        return 2*self.width+ 2*self.length
    def change_size (self, w, l):
        self.width = w 
        self.length = l 
    def identify(self):
        print("I am a rectangle")

rec1 = Rectangle(3,4)
print(rec1.area())

rec2 = Rectangle(4, 5)
rec3 = Rectangle(6, 7)
rec3.change_size(4,10)
print(rec2.perimeter())







