words=["python","java","c","javascript","Go"]
new=list(filter(lambda x:len(x)>3,words))
new1=list(map(lambda x:x.lower(),new))
print(new1)
print(len(new1))

total_chars = sum(map(len,new1))
print("Total number of characters:", total_chars)
