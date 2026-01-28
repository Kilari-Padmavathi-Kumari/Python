class Parent1():
    def fun(self):
        print("i am parent1")
class Parent2():
    def fun1(self):
        print("i am parent2")
class Child(Parent1,Parent2):
    def fun2(self):
        print("i am Child")
c=Child()
c.fun()
c.fun1()
c.fun2()
#p1=Parent1()
#p2=Parent2()
#p1.fun()
#p2.fun1()
