import csv,json
csvfile=open("csvdemo.csv",'r')
reader=csv.DictReader(csvfile)
rows=list(reader)

jsonfile=open("conveted.json",'w')
json.dump(rows,jsonfile,indent=4)
