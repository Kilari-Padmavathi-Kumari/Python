
class Outer:
    def show_outer(self):
        print("This is Outer class")

    # Inner class
    class Inner:
        def show_inner(self):
            print("This is Inner class")

# Creating object of inner class
obj = Outer.Inner()
obj.show_inner()


'''class Outer:
    def __init__(self):
        self.in_obj = self.Inner()

    def show(self):
        self.in_obj.display()
    # Inner class
    class Inner():
        def __init__(self):
          self.data = 'Inner Class'
    
        def display(self):
          print(self.data)
o=Outer()
o.show()'''