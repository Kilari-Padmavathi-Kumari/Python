class Parent:
    def __init__(self,d):
        self.data=d

    def show(self):
        print(self.data)

p=Parent(4)
p.show()
p.data=5
p.show()