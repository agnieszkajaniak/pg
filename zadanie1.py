# w niniejszym skrypcie znajduje sie rozwiazanie zadania wstepnego z zajec z programowania geoinformacyjnego
# skrypt wczytuje dane z pliku txt dotyczace powierzchni, liczby ludnosci oraz zaludnienia dla poszczegolnych powiatow 
# oraz przetworza je, tak aby mozna bylo
# wyliczyc statystyki dla poszczegolnych kolumn liczbowych
# nastepnie wyswietla statystyki w postaci sformatowanej
import csv
import numpy as np
 
# czytaj plik
def read_file():
    data = {}
    with open('dane.txt','rb') as csvfile:
        # czyta jako plik csv z tabulatorem jako separatorem
        reader = csv.reader(csvfile, delimiter='\t')
        # zamiana wierszy na kolumny dzieki funkcji zip
        for column in zip(*reader):
            data[column[0]] = column[1:]
 
    # zamiana string na float
    for column_name in ['Powierzchnia', 'Ludnosc','Zaludnienie']:
        data[column_name] = map(string_to_number, data[column_name])
 
    return data
 
def string_to_number(text):
    try:
        # zamien przecinek na kropke i zamien na float
        return float(text.replace(',','.'))
    except:
        # gdy nie uda sie zamienic na float zwroc 'NA'
        return 'NA'
 
def stats_for_array(array):
    # bierz pod uwage tylko wartosci liczbowe
    tab = np.array([i for i in array if i != 'NA'])
    # zwroc slownik podstawowych statystyk
    return { 'mean': np.mean(tab), 'median': np.median(tab), 'std': np.std(tab),
             'min' : np.amin(tab), 'max' : np.amax(tab) }
 
def get_stats(data):
    stats = {}
    # oblicz statystyki dla podanych kolumn
    for column_name in ['Powierzchnia', 'Ludnosc','Zaludnienie']:
        stats[column_name] = stats_for_array(data[column_name])
    return stats
 
def print_stats(stats):
    stats_names = ['std', 'max', 'min', 'mean', 'median']
 
    # wypisz naglowki kolumn
    print(" "*13 + " ".join(["%10s" % x for x in stats_names]))
    for key, value in stats.iteritems():
        # wypisz nazwe wiersza a nastepnie wartosci statystyk odpowiednio sformatowane
        print('%13s' % key + " ".join([('%10.1f' % value[x]) for x in stats_names]))
 
data = read_file()
stats = get_stats(data)
print_stats(stats)

# praca wykonana z Miloszem Rumianowskim i Martyna Walicka
