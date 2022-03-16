import random as rand
import pandas as pd

generate = False
print_to_csv = False

full_set = [1,4,7,3,2] #list()

subsets = list()

size_of_set = 100 # can change this

range_of_set = 2000 # can change this 

subset_size = 5 # can change this

number_of_subsets = 50 # can change this

if generate:

    for i in range(size_of_set):

        element = rand.randint(20, range_of_set) # was 0
        while element in full_set:
            element = rand.randint(20, range_of_set)
        full_set.append(element)

    #print(full_set)

    for i in range(number_of_subsets):
        a_subset = list()
        for j in range(subset_size):
            element = rand.choice(full_set)
            while element in a_subset:
                element = rand.choice(full_set)
            a_subset.append(element)
        subsets.append(a_subset)

    #print(subsets)
    #print(full_set)

if print_to_csv:
    subs = pd.DataFrame(subsets)
    print(subs)
    subs.to_csv("toy_sets.csv")
    s = pd.DataFrame(list(full_set))
    s.to_csv("full_toy_set.csv")