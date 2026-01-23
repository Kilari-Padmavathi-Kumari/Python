class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        if self.marks>=35:
            print('passed')
        else:
            print('not')
s=Student('ramu',67)
s.display()
        