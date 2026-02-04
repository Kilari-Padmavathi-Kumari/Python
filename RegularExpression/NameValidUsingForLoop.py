import re
names=["padma","padma kilari","padma123","padma_k"]
for i in names:
    if re.fullmatch("[A-Za-z ]+",i):
        print(i)