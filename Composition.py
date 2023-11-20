#Composition 

class Dog():
    def __init__ (self, name, breed,owner):
        self.name = name
        self.breed = breed 
        self.owner = owner 

class Person():
    def __init__(self, name):
        self.name = name 

#Instantiate a Person
Roberto = Person('Roberto')

#Instantiate a dog
George = Dog('George', 'Australian Shepherd', Roberto)

print(Roberto.name)
print(George.name)
print(George.owner.name)