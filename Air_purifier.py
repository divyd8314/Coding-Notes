class Air_purifier():
    def __init__(self, level, on_off, filter, carbon, recycle):
        self.level = 0
        self.on_off = False 
        self.filter = 0
        self.carbon = 0
        self.recycle = False 
    def low_level(self, level):
        if self.level>0:
            self.level=self.level-1
    def high_level(self, level):
        if self.level<=3:
            self.level=self.level+1
    def On(self):
        if self.power == True:
            self.power==False 
            return self.power
        if self.power==False:
            self.power==True 
            return self.power
        self.on_off = True 
    def HEP_filter(self, filter):
        if filter>=10:
            print("Replace filter immediately")
        self.filter = self.filter
    def carbon_filter(self, carbon):
        if carbon>=6:
            print("Replace the carbon filter immediately")
        self.carbon=self.carbon+carbon
    
testcase = (2, True)





