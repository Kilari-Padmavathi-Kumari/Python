class Parent():
    def fun(self):
        print("i am parent")
class Child(Parent):
    def fun1(self):
        print("i am Child")
class Gchild(Child):
    def fun2(self):
        print("i am grand child")
gc=Gchild()
gc.fun()
gc.fun1()
gc.fun2()