import csv
file=open("csvdemo.csv",'r')
reader=csv.DictReader(file)
for row in reader:
    print(row['name'],row['age'])

