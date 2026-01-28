class Parent:
    def __init__(self,d):
        self.__data=d

    def show(self):
        print(self.__data)

p=Parent(4)
p.show()
p.__data=5
p.show()




class Parent:
    def __init__(self,d):
        self.__data=d

    def show(self):
        print(self.__data)

p=Parent(4)
p.show()
p._Parent__data=5
p.show()



