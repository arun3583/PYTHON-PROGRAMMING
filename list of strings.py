rows = []
import csv
f = open("username.csv", "r")
csvreader = csv.reader(f)
for row in csvreader:
	row=str(row)
	rows.append(row)
print(rows)