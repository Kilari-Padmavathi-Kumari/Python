class Parent:
    def __init__(self, a, b):
        self.__a = a    # private
        self._b = b     # protected

class Child(Parent):
    def show(self):
        # print(self.__a)   not accessible
        print(self._b)     # accessible

c = Child(10, 20)
c.show()
