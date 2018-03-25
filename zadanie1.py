import csv
data = {}
with open('dane.txt','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for column in zip(*reader):
        data[column[0]] = column[1:]

