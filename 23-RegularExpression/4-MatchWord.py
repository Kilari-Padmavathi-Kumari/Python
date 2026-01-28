import re
str="sat,hat,mat,pat"
allstr=re.findall("[shmp]at",str)
for i in allstr:
    print(i)
print("\n")
import re
str="sat,hat,mat,pat"
allstr=re.findall("[h-m]at",str)

for i in allstr:
    print(i)