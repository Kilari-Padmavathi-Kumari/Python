'''names=("padma","kavya","josh")
comps=("dell","it","doctor")
zipped=list(zip(names,comps))
print(zipped)
'''
'''
names=("padma","kavya","josh")
comps=("dell","it","doctor")
zipped=dict(zip(names,comps))
print(zipped)'''


names=("padma","kavya","josh")
comps=("dell","it","doctor")
zipped=list(zip(names,comps))
print(zipped)

for (a,b) in zipped:
    print(a,b) 
