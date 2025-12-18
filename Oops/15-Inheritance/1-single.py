'''
Docstring for Oops.15-Inheritance.1-sample
single Inheritance
multilevel Inheritance
multiple Inheritance
hierachical Inheritance

'''

class Parent():
    def fun(self):
        print("i am parent")
class Child(Parent):
    def fun1(self):
        print("i am Child")
c=Child()    
c.fun1()
c.fun()