num=[10,15,20,25,30,35,40]

result={}

for i in num:
    if i%2==0:
        result[i]='even'
    else:
        result[i]='odd'
print(result)