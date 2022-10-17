class DemoClass:
    def __init__(self, arg):
        self.arg = arg

class DemoMath:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    

x = DemoMath(5,6)
print(x.add())
print(x.sub())

class RateOfIntrest:
    intrest = 0.06 #class varible

    def __init__(self, name, loan):
        self.name = name #insident varible
        self.loan = loan #insident varible
    
    def calc(self):
        x = self.loan * self.intrest
        print("Total intrest: ", x)

p1 = RateOfIntrest('Jhon', 500000)
p1.calc()

p2 = RateOfIntrest('Joe', 500000)
p2.intrest = 0.05
p2.calc()

class ChildBank(RateOfIntrest):
    def __init__(self, name, loan):
        super().__init__(name, loan)
    
    def getIntrest(self):
        print('intrest is :',self.intrest)

c1 = ChildBank('Test', 500000)
c1.intrest = 0.045
c1.getIntrest()
c1.calc()