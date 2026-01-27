import math
data=[1,2,2,3,4,4,5,6,7,7]
set1=set(data)
print(set1)
for i in set1:
    if i%2==1:
        print(math.sqrt(i))