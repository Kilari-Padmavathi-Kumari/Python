lst=[1,2,3,2,4,3,3,2,2,4,1,4]
freq={}

for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)