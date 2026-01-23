def fun(*a):
    print("arg",a)          #orbitary arguments
fun(1,2,3)

def fun(**a):
    print("karg",a)        #key argments
fun(a=1,b=2)

def stud(name,age):
    print(name,age)
stud(name="padma",age=23)