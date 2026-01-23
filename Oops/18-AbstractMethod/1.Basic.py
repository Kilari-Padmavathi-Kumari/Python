from abc import ABC,abstractmethod
class Parent(ABC):
    def meth1(self):
        print('i am meth--1')
    @abstractmethod
    def meth2(self):
        pass

class Child(Parent):
    def meth3(self):
        print('i am meth--3')
    
    def meth2(self):
        print('i am meth--2')

c=Child()
c.meth3()
c.meth2()
c.meth1()