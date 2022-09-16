# there are 2 types of variables, class variables declared in a class and instance variables declared in constructors
# instance variables must be called with the "self" obj name while class variables can either use "self" of class name
# to call a class you must create an object

class calculator:
    num = 100

    def __init__(self, a, b):
        self.firstInt = a
        self.secondInt = b
        print("This demonstrates that constructors are printed automatically")

    def getData(self):
        print("Salma is trying to learn OOP")

    def summation(self):
        return self.firstInt + self.secondInt + calculator.num


obj = calculator(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.summation())

obj1 = calculator(15, 13)  # syntax to create objects in python
obj1.getData()
print(obj1.summation())