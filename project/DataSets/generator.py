import random as rand
import pandas as pd
import csv

generate = True
print_to_csv = True

full_set = list() #[1,4,7,3,2] 

subsets = list()

size_of_set = 1000 # can change this 100

range_of_set = 100000 # can change this 20000

#subset_size = 5 # can change this

number_of_subsets = 250 # can change this 50

if generate:

    for i in range(size_of_set):

        element = rand.randint(1, range_of_set) # was 20
        while element in full_set:
            element = rand.randint(1, range_of_set)
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

    with open('project/DataSets/sets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for set_ in subsets:
            writer.writerow(set_)

    with open('project/DataSets/sets_key.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(full_set)
        

    #s = pd.DataFrame(list(full_set))
    #s.to_csv("full_toy_set.csv")