class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"name is : {self.name} age is : {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        
    def display(self):
        super().display()
        print(f"name is : {self.name} , age is : {self.age}, marks are {self.marks}")

s=Student("padma",23,98)
s.display()


