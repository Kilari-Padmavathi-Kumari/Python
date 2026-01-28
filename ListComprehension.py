'''list=[1,2,3,4,5,6,7]
new_list=[x*5 for x in list]
print(new_list)'''

'''list=[1,2,3,4,5,6,7]
new_list=[x%2==0 for x in list]
print(new_list)'''


'''new=[x for x in range(20) if x%2==0]
print(new)'''


num=[1,2,3,4,5,6]
new=["even" if n%2==0 else "odd" for n in num]
print(new)