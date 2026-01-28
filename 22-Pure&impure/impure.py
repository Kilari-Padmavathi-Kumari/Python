x=10
def add(num):
    return num+x
print(add(3))


total=0
def add(num):
    global total
    total +=num
obj=add(8)
print(obj)