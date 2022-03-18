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

# open file in read mode
with open('project/DataSets/toy_sets1.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        sample_population.append(list(map(int, row)))

#print(sample_population)

genetic_alg = ga.GeneticAlgorithm(sample_population, 5, 17, (0, 20000))

while(True):
    genetic_alg.propagate('w', 'u', 1, 3, 0.05)

        