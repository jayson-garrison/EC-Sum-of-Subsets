import numpy as np
import pandas as pd
import random as rand
from csv import reader

from GeneticAlgorithm import GeneticAlgorithm as ga

# sample_population_df = pd.read_csv("project/DataSets/toy_sets.csv")

# sample_population_df = sample_population_df[:][:]

# print(sample_population_df)

# print(sample_population_df.values.tolist())

sample_population = list()

key = list()

# open file in read mode
with open('project/DataSets/sets.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        sample_population.append(list(map(int, row)))

# open file in read mode
with open('project/DataSets/sets_key.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # for element in row:
        #     key.append(map(int, element))
        key = (list(map(int, row)))

#print(sample_population)
# print(key)
# print(key[0])

if True:
    #genetic_alg = ga.GeneticAlgorithm(sample_population, 5, 17, key)
    genetic_alg = ga.GeneticAlgorithm(sample_population, 10, 1300000, key)

    iter = 0
    while(iter < 150):
        genetic_alg.propagate('w', 'u', 'flip', 1, 10, 0.25)
        iter += 1

        