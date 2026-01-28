

class Outer:
    def __init__(self):
        self.in_obj=self.Inner()

    def show(self):
        self.in_obj.display()

    class Inner():
        def __init__(self):
          self.data='Inner Class'
    
        def display(self):
          print(self.data)
o=Outer()
o.show()