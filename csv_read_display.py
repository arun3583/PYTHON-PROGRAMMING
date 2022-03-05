import csv
d={1:'Denny',2:'Denis',3:'Don',4:'Dia'}
with open("sample.csv","w") as f1:
    csvrdr=csv.writer(f1)
    for item in d.items():
        csvrdr.writerow(item)
with open("sample.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(" ".join(row))
