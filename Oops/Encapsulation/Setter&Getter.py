class Person:
    def __init__(self):
        self.__age = 0   # private variable

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p = Person()

p.set_age(25)
print("Age:", p.get_age())

p.set_age(-5)   # invalid
