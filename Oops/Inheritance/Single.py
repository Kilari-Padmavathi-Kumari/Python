'''
Docstring for Oops.15-Inheritance.1-sample
single Inheritance
multilevel Inheritance
multiple Inheritance
hierachical Inheritance

'''
# Parent class
class Parent():
    def fun(self):
        print("i am parent")
# Child class
class Child(Parent):
    def fun1(self):
        print("i am Child")
# Creating child object
c=Child()    
c.fun1()
c.fun()