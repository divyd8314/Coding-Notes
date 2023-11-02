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
