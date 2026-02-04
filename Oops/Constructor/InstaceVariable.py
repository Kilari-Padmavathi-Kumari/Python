class Test:
    def __init__(self,a):
        self.a=a
    def variable(self):
        self.b=20

    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)
t=Test(10)
t.variable()
t.c=30
t.show()