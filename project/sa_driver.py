from csv import reader
from random import sample
from SimulatedAnnealing import SimulatedAnnealing as sa

sample_population = list()

key = list()

fname = 'dataset1.csv'
fkname = 'dataset1_key.csv'
dirname = 'dataset1'
# open file in read mode
with open('project/DataSets/' + fname, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object

    sample_population = list(map(int, csv_reader.__next__()))
    sample_population = list(map(int, csv_reader.__next__()))

# open file in read mode
with open('project/DataSets/' + fkname, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # for element in row:
        #     key.append(map(int, element))
        key = (list(map(int, row)))

#print(sample_population)
#print(key)
# print(key[0])

k = 2500 # 2500 2500000 25000000

perts = (3, 'fredinc') # (2, 'fredinc')

simulated_anneal = sa.SimulatedAnnealing(k, key, sample_population)

simulated_anneal.anneal(dirname, perts, 1000, 1000, .95, 1.01)