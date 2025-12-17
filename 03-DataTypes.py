'''
Docstring for DataTypes
int(1,-1)
boolean
float
complex

'''
a=1
b=-1
print(a,b)
print(type(a),type(b))

a=True
b=False
print(a,b)
print(type(a),type(b))
print(True==1,False==0)

'''
type conversion
int()
float()
bool()
str()

data lose-> explicit type conversion
no data lose -> implicit type conversion
'''
a=2
print(float(a))

b=5.5
print(int(b))