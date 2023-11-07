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

#OOP and practial modelling 
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False 
    def turnOn(self):
        self.switchIsOn = True 
    def turnOff(self):
        self.switchIsOn = False 
    def show(self):
        print('Status of light', self.switchIsOn)
light1 = LightSwitch()
light1.show()
light1.turnOn()
light1.show()

#Create class DimmerSwitch() with same properties as previous example
#Include another property called brightness
#The brightness can go between 1-10
#The brightness should be zero when an object is created 
#Should be able to raise and lower brightness 
#Method show() should have two outputs, 1. Switch is on?, 2. Brightness is ...

class DimmerSwitch():
    def __init__(self):
        self.brightness = 0
        self.SwitchisOn = False 
    def turnOn(self):
        self.SwitchisOn = True
    def turnOff(self):
        self.SwitchisOff = False 
    def raiseBrightness(self, x):
        if self.brightness<10:
            self.brightness+=x
    def lowerBrightness(self,x):
        if self.brightness>0:
            self.brightness-=x
    def show(self):
        print('Switch is on', self.SwitchisOn,
              'Brightness is ', self.brightness)
        

light1=DimmerSwitch()
light2 = DimmerSwitch()
light1.turnOn()
light1.raiseBrightness(2)
light1.show()

#Real world bank account example 
class Account():
    def __init__(self, name, balance, password):
        self.name = name 
        self.balance = balance 
        self.password = password 
    def deposit(self, amount, password):
        if password != self.password:
            print("sorry incorrect password")
            return None
        if amount<0:
            print("Deposit unsuccessful, amount not valid")
            return None 
        self.balance = self.balance+amount
        return self.balance 
    def withdraw(self, amount, password):
        if password!=self.password:
            print("sorry incorrect password")
            return None 
        if amount>self.balance:
            print("Amount more than in account")
            return None 
        if amount<0:
            print("Withdrawal unsuccessful, amount not valid")
            return None 
        self.balance = self.balance-amount
        return self.balance 
    def balance(self, password):
        if password!=self.password:
            print("sorry incorrect password")
            return None 
        return self.balance 
    def show(self, password):
        print('Name: ', self.name)
        print('Balance: ', self.balance)
        print("Password: ", self.password)


