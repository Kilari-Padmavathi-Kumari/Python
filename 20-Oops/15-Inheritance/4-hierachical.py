class Parent1:
    def fun(self):
        print("i am parent1")
class Child1(Parent1):
    def fun1(self):
        print("i am child1")
class Child2(Parent1):
    def fun2(self):
        print("i am Child2")
c1=Child1()
c2=Child2()
c1.fun()
c1.fun1()
c2.fun()
c2.fun2()