class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('hello, my name is', self.name)
me = Person('fariz')
me.say_hi()

class Calculator:
    def __init__ (self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def subtract(self):
        result = self.num1 - self.num2
        return result
    def multiply(self):
        result = self.num1 * self.num2
        return result
    def divide(self):
        result = self.num1/self.num2
        return result
count = Calculator(5,4)
print(count.add())
