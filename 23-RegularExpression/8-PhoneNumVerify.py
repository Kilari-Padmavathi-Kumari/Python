import re
#\w [a-zA-Z0-9]
#\W [^a-zA-Z0-9]

phn="412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("it is valid")
