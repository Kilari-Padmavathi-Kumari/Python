class Method():
    a=30
    print(a)
    def fun(self):
        print("function with in the class")
b=Method()  # object create
b.fun()     #method calling
print(b.a)  # variable callng
