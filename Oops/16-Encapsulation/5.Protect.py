class Parent:
    def __init__(self,d):
        self._data=d

    def show(self):
        print(self._data)

class Child(Parent):
    def __init__(self, d):
        super().__init__(d) 
    def disply(self):
        print(self._data)

p=Child(4)
p.show()
p._data=5
p.show()
p.disply()



