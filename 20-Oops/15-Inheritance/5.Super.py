class Parent:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return self.length*self.breadth
    
class Child(Parent):

    def __init__(self,l,b,h):
        self.height=h
        super().__init__(l, b)
    def volume(self):
        return self.length*self.breadth*self.height
    
c=Child(2,3,4)
print(c.volume())
print(c.area())

  
    
        