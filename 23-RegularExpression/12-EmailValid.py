import re
emails = [
    "padma@gmail.com",
    "padma123@yahoo.in",
    "padma@com",
    "padma@gmail"
]

for i in emails:
    if re.fullmatch(r"[a-zA-Z0-9+-]+@[a-zA-z]+\.[a-zA-Z]{2,}",i):
        print(i)