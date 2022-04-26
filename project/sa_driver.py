from csv import reader
from random import sample
from SimulatedAnnealing import SimulatedAnnealing as sa

sample_population = list()

key = list()

fname = 'dataset3.csv'
fkname = 'dataset3_key.csv'
dirname = 'dataset3'
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

k = 25000000 # 2500 2500000 25000000

perts = (2, 'flip') # (1, 'fredinc')

simulated_anneal = sa.SimulatedAnnealing(k, key, sample_population)

simulated_anneal.anneal(dirname, perts, 1000, 1000, .95, 1.01)