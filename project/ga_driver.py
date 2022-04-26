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

fname = 'dataset1.csv'
fkname = 'dataset1_key.csv'
dirname = 'dataset1'
# open file in read mode
with open('project/DataSets/' + fname, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        sample_population.append(list(map(int, row)))

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
# print(key)
# print(key[0])

if True:
    # for toy
    #genetic_alg = ga.GeneticAlgorithm(sample_population, 5, 17, key)

    # for sets (std)
    # genetic_alg = ga.GeneticAlgorithm(sample_population, 10, 1300000, key)
    #genetic_alg = ga.GeneticAlgorithm(sample_population, 5, 2500, key)
    #genetic_alg = ga.GeneticAlgorithm(sample_population, 10, 1300000, key)
    #genetic_alg = ga.GeneticAlgorithm(sample_population, 10, 1300000, key)

    # others

    iter = 0
    stop = 50 # 50 100 150
    configurations1 = [

        ('w','u','flip', 10, 2, 0.05),
        ('w','n-pt','flip', 10, 2, 0.05),
        ('w','u','fredinc', 10, 2, 0.05),
        ('w','n-pt','fredinc', 10, 2, 0.05),

        ('r','u','flip', 10, 2, 0.05),
        ('r','n-pt','flip', 10, 2, 0.05),
        ('r','u','fredinc', 10, 2, 0.05),
        ('r','n-pt','fredinc', 10, 2, 0.05),


    ]
    configurations2 = [

        ('w','u','flip', 50, 2, 0.05),
        ('w','n-pt','flip', 50, 2, 0.05),
        ('w','u','fredinc', 50, 2, 0.05),
        ('w','n-pt','fredinc', 50, 2, 0.05),

        ('r','u','flip', 50, 2, 0.05),
        ('r','n-pt','flip', 50, 2, 0.05),
        ('r','u','fredinc', 50, 2, 0.05),
        ('r','n-pt','fredinc', 50, 2, 0.05),

    ]
    configurations3 = [

        ('w','u','flip', 100, 2, 0.05),
        ('w','n-pt','flip', 100, 2, 0.05),
        ('w','u','fredinc', 100, 2, 0.05),
        ('w','n-pt','fredinc', 100, 2, 0.05),

        ('r','u','flip', 100, 2, 0.05),
        ('r','n-pt','flip', 100, 2, 0.05),
        ('r','u','fredinc', 100, 2, 0.05),
        ('r','n-pt','fredinc', 100, 2, 0.05),

    ]

    k = 2500 # 2500 2500000 25000000

    try:
        for config in configurations1:
            iter = 0
            convergence = False
            genetic_alg = ga.GeneticAlgorithm(sample_population, 5, k, key)
            #genetic_alg = ga.GeneticAlgorithm(sample_population, 10, k, key)
            #genetic_alg = ga.GeneticAlgorithm(sample_population, 100, k, key)
            while(iter < stop and not genetic_alg.trapped() and not convergence):
                avg = genetic_alg.propagate(dirname, fname, config[0], config[1], config[2], config[3], config[4], config[5])
                iter += 1
                epsilon = (k - avg) / k
                if (epsilon > .999 and epsilon <= 1.0):
                    convergence = True
                if iter == stop or convergence:
                    genetic_alg.solution_export()
    except KeyboardInterrupt:
        print(f'\nexception: interrupt- terminating algorithm, dumping final solution to out.')
        genetic_alg.solution_export()
        exit()

        