
import csv

rows=[
    {'name':'padma','age':30},
     {'name':'kavya','age':42},

]
file=open("csvdemo.csv",'w')
fieldnames=['name','age']
writer=csv.DictWriter(file,fieldnames=fieldnames)
writer.writeheader()
writer.writerows(rows)
