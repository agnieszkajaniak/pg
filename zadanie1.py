import csv
data = {}
with open('dane.txt','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for column in zip(*reader):
        data[column[0]] = column[1:]


def string_to_number(text):
    try:
        return float(text.replace(',','.'))
    except:
        return 'NA'

for column_name in ['Powierzchnia', 'Ludnosc','Zaludnienie']:
    data[column_name] = map(string_to_number, data[column_name])

