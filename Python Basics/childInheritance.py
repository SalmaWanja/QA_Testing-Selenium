from oopdemo import calculator


class ChildInheritance(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self, 15,20)

    def getCompleteData(self):
        return self.num2 + self.summation()


obj = ChildInheritance()
print(obj.getCompleteData())
