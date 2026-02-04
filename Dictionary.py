d={}
print(type(d))

d={1:'abc',22:'padma','kavya':'josh'}
print(d[1])

'''
get 
update
values
keys
items
'''
d={1:'abc',22:'padma','kavya':'josh'}
#print(d.get(1))
#print(d.keys())
#print(d.values())
#print(d.items())
d.update({4:'padma'})
print(d)



for i in {1:'abc',22:'padma','kavya':'josh'}.items():
    print(i)

for i,j in {1:'abc',22:'padma','kavya':'josh'}.items():
    print(i,j)

