import re
str="hat,mat,rat,pat"
regex=re.compile("[r]at")
str=regex.sub("food",str)
print(str)