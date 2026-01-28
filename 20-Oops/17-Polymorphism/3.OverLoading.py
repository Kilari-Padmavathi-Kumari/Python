
def sum(a,b):
        return a+b
def sum(a,b,c):          #Python, method overloading does not work in the traditional way
       return a+b+c    #Python does not support multiple methods with the same name and different parameters in the same class.
                         #If you define a method more than once, the last definition overrides the previous ones.
print(sum(2,3,5))
        