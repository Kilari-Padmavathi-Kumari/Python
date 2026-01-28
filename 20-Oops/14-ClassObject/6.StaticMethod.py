class Test:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    @staticmethod
    def cal_area(l,b):
        return l*b
r1=Test(3,4)
print(Test.cal_area(4,5))