#variable=value
a=10
print(a)


#a,b,c=1 it is not possible  
#a=b=c=1
#c=1,2,3,4  it is possible  o/p=(1,2,3,4)

c=1,2,3,4,5
print(c)

a=b=c=11
print(a,b,c)

#using id method
a=23
print(id(a))            #memory address

a,b,c=1,1,1
print(id(a),id(b),id(c))

#case sensitive
padma=1
PADMA=22
print(padma)

name,price,qty='soap',12.75,5
print(name,price,qty)