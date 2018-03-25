import csv
import numpy as np

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


def stats(array):
    tab = np.array([i for i in array if i != 'NA'])
    return { 'mean': np.mean(tab), 'median': np.median(tab), 'std': np.std(tab), 
             'min' : np.amin(tab), 'max' : np.amax(tab) }

statistics = {}
for column_name in ['Powierzchnia', 'Ludnosc','Zaludnienie']:
    statistics[column_name] = stats(data[column_name])


