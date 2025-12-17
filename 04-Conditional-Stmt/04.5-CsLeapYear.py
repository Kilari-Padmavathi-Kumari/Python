







year=int(input("Enter number:"))

if year%100==0:
    if year%400==0:
        print("Laep Year")
    else:
        print("not")
elif year%4==0:
    print("Laep Year")
else:
    print("not")



