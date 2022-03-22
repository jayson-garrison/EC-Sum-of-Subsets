import random as rand
import pandas as pd
import csv

generate = True
print_to_csv = True

full_set = [1,4,7,3,2] #list()

subsets = list()

size_of_set = 1000 # can change this 100

range_of_set = 20000 # can change this 2000

#subset_size = 5 # can change this

number_of_subsets = 150 # can change this 50

if generate:

    for i in range(size_of_set):

        element = rand.randint(20, range_of_set) # was 0
        while element in full_set:
            element = rand.randint(20, range_of_set)
        full_set.append(element)

    #print(full_set)

    for i in range(number_of_subsets):
        a_subset = list()
        subset_size = rand.randint(1, size_of_set)
        for j in range(subset_size):
            element = rand.choice(full_set)
            while element in a_subset:
                element = rand.choice(full_set)
            a_subset.append(element)
        subsets.append(a_subset)

    #print(subsets)
    #print(full_set)

if print_to_csv:
    # subs = pd.DataFrame(subsets)
    # print(subs)
    # subs.to_csv("project/DataSets/toy_sets.csv")

    with open('project/DataSets/toy_sets1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for set_ in subsets:
            writer.writerow(set_)

    with open('project/DataSets/toy_sets1_key.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(full_set)
        

    #s = pd.DataFrame(list(full_set))
    #s.to_csv("full_toy_set.csv")