from pickle import bytes_types
import numpy as np
from Utils.GenericGA import GenericGA
import random as rand
import scipy.stats as ss

import os

from matplotlib import pyplot as plt

from GeneticAlgorithm.Pool import Pool
from GeneticAlgorithm.Chromosome import Chromosome

class GeneticAlgorithm(GenericGA):

    def __init__(self, init_population, num_elites, k, set_):
        """
        init the Genetic Algorithm

        @param init_population -> the initial population of solutions, is a list of lists
        @param num_elites -> the number of elites to keep in the pool each generation
        @param k -> desired sum for all elements in any subset to add up to be leq than
        @param set_ -> the whole set which is the basis of the init_population
        """
        super().__init__()
        self.trap = False
        self.gen = 0
        # number of elites to keep
        self.num_elites = num_elites
        # upper limit
        self.set_ = set_
        # desired k
        self.k = k
        # init the pool given a read csv
        self.pool = Pool()
        # create chromosomes
        for soln in init_population:
            #print(soln)
            self.pool.add( Chromosome(self.set_, self.k, soln) )
        

    def select_parents(self, selection = 'w' ):
        """
        @param: pool -> a pool of chromosomes
        @param selection 
        
                         -> w for roulette wheel selection (default)

                         -> r for rank selection

                         -> t for tournament

        @returns a list of tuples of the selected parents for crossover

        length of returned list is the same as the size of the current pool
        """
        super().select_parents()

        if selection == "w":
    
            total_fitness = 0
            min_cum_fitness = 0
            parent_set = list()
            selection_probabilities = list()

            # determine total cumulative fitness of all chromosomes
            #total_fitness = sum(self.pool.poolAsList())

            total_fitness = 0
            for creature in self.pool.poolAsList():
                total_fitness += creature.getFitness()

            # determine the aggregate reverse fitness in the minimization
            for soln in self.pool.poolAsList():
                # if we have soln.getFitness() == 0 then we have the soln!
                if (soln.getFitness() == 0):
                    print("*****Optimal Solution Found!")
                    print(soln.getSolution())

                    # report
                    self.statistics()
                    self.solution_export()

                    return -1
                else:
                    min_cum_fitness += total_fitness / soln.getFitness() 

            # calculate the weights based on the minimization
            for soln in self.pool.poolAsList():
                selection_probabilities.append( (total_fitness / soln.getFitness() ) / min_cum_fitness)

            # determine all parent pairs using wheel selection
            for amt in range(self.pool.size() - self.num_elites):

                parents = (rand.choices(self.pool.poolAsList(), weights=selection_probabilities)[0],\
                        rand.choices(self.pool.poolAsList(), weights=selection_probabilities)[0] )

                parent_set.append(parents)

            # return list of length pool.size() - num_elites of parent pairs for crossover
            #print(parent_set[0])
            return parent_set

        elif selection == 'r':

            # know the number of chromosomes, rank is out of that
            # determine the rank of each chromosome by finding the min
            # associate

            fitness_list = list()
            
            # determine the fitnesses of all the chromosomes
            for creature in self.pool.poolAsList():
                fitness_list.append(creature.getFitness())

            # rank the weights using scipy
            rank_weights = ss.rankdata(fitness_list, method='ordinal')
            #print(rank_weights[0])

            # the length of chromosomes in the pool, fix the rank to reflect
            # the min fitness as the best
            diff = self.pool.size() + 1
            #print(diff)
            new_rank_weights = list()

            total = 0
            for r in range(self.pool.size() + 1):
                total += r

            for idx, value in enumerate(rank_weights):
                new_rank_weights.append( (diff - value) / total )
                #print((diff - value) / fit_sum)
                #print(new_rank_weights[idx],end=" ")
            #print(sum(new_rank_weights))
            

            # make the parents
            # determine all parent pairs using wheel selection
            parent_set = list()
            for amt in range(self.pool.size() - self.num_elites):

                parents = (rand.choices(self.pool.poolAsList(), weights=new_rank_weights)[0],\
                        rand.choices(self.pool.poolAsList(), weights=new_rank_weights)[0] )

                parent_set.append(parents)

            return parent_set
            # rank_weights = np.zeros(self.pool.size())

            # fitness_list = list()
            # for creature in self.pool.poolAsList():
            #     fitness_list.append(creature.getFitness())
            # removal_list = fitness_list.copy()
            # #copy_pool = self.pool.poolAsList()
            # for _ in range(len(fitness_list)):
            #     best = min(removal_list)
            #     rank_weights[fitness_list.index(best)]

           
            pass
        elif selection == 't':
            pass
        else:
            print("error: invalid selection method")    


    def crossover(self, parents, technique = 'u', n = 1):
        """
        given a set of parents, crossover using a given technique

        @param parents -> the list of parents to crossover, is a list of tuples (parent1, parent2)
        @param technique 
                        -> u for uniform (default)

                        -> n-pt for n-point
        @param n -> n used for n-pt

        @returns the child pool
        """
        super().crossover()
        
        if technique == 'u':
            child_pool = list()
            for pair in parents:
                child = np.zeros(len(self.set_))
                for idx in range(len(self.set_)):
                    which = rand.randint(0,1)
                    if which == 0:
                        #print(type(pair[0]))
                        #print(pair[0])
                        child[idx] = pair[0].getChromosome()[idx]
                    else:
                        #print(type(pair[1]))
                        #print(pair[1])
                        child[idx] = pair[1].getChromosome()[idx]

                child_pool.append(Chromosome(self.set_, self.k, list(), child))

            return child_pool

        elif technique == 'n-pt':
            # the index to partition the parents
            child_pool = list()

            
            for pair in parents:
                pdex = int(self.pool.get(0).vectorSize() / (n + 1))
                which = 0
                idx = 0

                child = list()
                #print(pair[0].getChromosome())
                #print(pair[1].getChromosome())
                # do while not done
                count = 0
                while count < n + 1:
                    if which == 0:
                        which = 1
                        # handle the end case
                        if count == n:
                            section = pair[0].getChromosome()[idx:]
                            for val in section:
                                child.append(val)
                        else:
                            section = pair[0].getChromosome()[idx:idx+pdex]
                            for val in section:
                                child.append(val)
                            #child.append(pair[0].getChromosome()[idx:idx+pdex])

                        idx = idx + pdex
                    else:
                        which = 0
                        # handle the end case
                        if count == n:
                            section = pair[1].getChromosome()[idx:]
                            for val in section:
                                child.append(val)

                        else:
                            section = pair[1].getChromosome()[idx:idx+pdex]
                            for val in section:
                                child.append(val)

                        idx = idx + pdex

                    count += 1
                # convert list to np.array and make a chrome``
                child_chrome = np.array(child)
                #print(child_chrome)
                #exit()
                child_pool.append(Chromosome(self.set_, self.k, list(), child_chrome))
            
            return child_pool

        else:
            print("error: invalid crossover technique")
            exit()

    def mutation(self, num_bits, method, rate = 0.05):
        """
        mutate each chromosome in the pool given a probability

        @param num_bits -> upon a successful mutation, the number of bits to conider in the chromosome

        @param method -> method of mutation
                        
                        flip: flip a number of bits

                        fredinc: force reduction-increase, forcibly reduce and increase active/inactive bits 

        @param rate -> a number between 0 and 1 for the mutation rate (.05 is common)
        """
        super().mutation()

        for chrome in self.pool.poolAsList():
            mutation_chance = rand.randint(1, 100)
            flips = set()
            # mutation sucessful
            if mutation_chance <= rate * 100:
            
                if method == 'flip':
                
                    # generate a set of random indicies to flip
                    while (len(flips) < num_bits):
                        flip_index = rand.randint(0, chrome.vectorSize() - 1)
                        while flip_index in flips:
                            flip_index = rand.randint(0, chrome.vectorSize() - 1)
                        flips.add(flip_index)
                    
                    for idx in flips:
                        if chrome.getChromosome()[idx] == 0:
                            chrome.getChromosome()[idx] == 1
                        else:
                            chrome.getChromosome()[idx] == 0

                    # update the solution to reflect the mutated chromosome        
                    chrome.updateSolution()

                elif method == 'fredinc':

                    # seperate ones and zeros
                    ones = list()
                    zeros = list()
                    for idx, value in enumerate(chrome.getChromosome()):
                        if value == 1:
                            ones.append(idx)
                        else:
                            zeros.append(idx)

                    which = rand.randint(1, 100)

                    reduce = list()

                    if which < 90 and len(ones) != 0:
                        # force reduction
                        # pick num_bits randomly

                        item = rand.choice(ones)
                        i = 0

                        if len(ones) <= num_bits:
                            # proceed
                            for index in ones:
                                chrome.getChromosome()[index] = 0
                        else:
                            while item not in reduce and i < num_bits:
                                reduce.append(item)
                                item = rand.choice(ones)
                                i += 1

                            for index in reduce:
                                chrome.getChromosome()[index] = 0
                        
                    else:
                        # force increase

                        if len(zeros) == 0:
                            break

                        item = rand.choice(zeros)
                        i = 0

                        if len(zeros) <= num_bits:
                            # proceed
                            for index in zeros:
                                chrome.getChromosome()[index] = 1
                        else:
                            while item not in reduce and i < num_bits:
                                reduce.append(item)
                                item = rand.choice(zeros)
                                i += 1

                            for index in reduce:
                                chrome.getChromosome()[index] = 1
                        
                    chrome.updateSolution()
                    
                else:
                    print('error: invalid mutation technique')
                    exit()

    def generation(self, children):
        """
        after selection, crossover, then mutation, a new generation is formed of the children with the elites
        
        thus, the pool is reformed

        @param children -> the children to reform the pool with and create a new generation
        """
        ## create the new pool with all children
        new_pool = Pool(children)
        # find the elites, add them to new pool

        # list of all fitnesses
        # MOVED TO PROPAGATE!

        # find the elites, add them to new pool
        for _ in range(self.num_elites):
            elite_fitness = min(self.fitnesses) # min!!
            elite = self.pool.get( self.fitnesses.index(elite_fitness) )
            new_pool.add(elite)
            self.fitnesses.remove(elite_fitness)

        # can add past pools to a generations list?
        #self.pool.removeAll()
        self.pool = new_pool
    def propagate(self, dirname, filename, selection_method, crossover_technique, mutation_method, n = 1, num_bits = 1, mutation_rate = 0.05 ):
        """
        propagate the genetic algorithm one generation forward.

        @param selection_method -> method used in selecting parents

                                -> w for roulette wheel

                                -> r for rank

                                -> t for tournament
        
        @param crossover_technique -> technique used for crossover

                                -> u for uniform

                                -> n-pt for n-point
        @param n -> n used for the number of split points if using n-pt crossover (1 is standard)
        
        @param num_bits -> number of bits to mutate upon successful mutation (1 is standard)

        @param mutation_rate -> the mutation rate (0.05 is standard)
        
        """
        
        # print the stats for generation 0
        if self.gen == 0:
            self.path = f'project/GeneticAlgorithm/Visuals/{dirname}/ga_{filename}_S-{selection_method}_X-{crossover_technique}_M-{mutation_method}_n-{n}_NFlips-{num_bits}_Mrate-{mutation_rate}/'
            exists = os.path.exists(self.path)
            if not exists:
                os.makedirs(self.path)
                print('DIR CREATED')

            # remove all files in dir
            else:
                for file in os.listdir(self.path):
                    os.remove(self.path + file)
            
            
            self.fitnesses = list()
            for chrome in self.pool.poolAsList():
                self.fitnesses.append(chrome.getFitness())

            avg = self.statistics()
            self.gen += 1

        # define the list of fitnesses
        self.fitnesses = list()
        for chrome in self.pool.poolAsList():
            self.fitnesses.append(chrome.getFitness())

        # select parents
        parents = self.select_parents(selection_method)
        
        if parents != -1:
            
            # crossover
            childs = self.crossover(parents, crossover_technique, n)
            # generate
            self.generation(childs)
            # mutate
            self.mutation(num_bits, mutation_method, mutation_rate)
            # stats
            avg = self.statistics()

            self.gen += 1

            return avg
        else:
            self.optimal()
            return self.statistics()

    def statistics(self):
        """
        prints statistics regarding the genetic algorithm process in solving the current problem
        """
        # print average fitness in this generation
        avg = sum(self.fitnesses) / len(self.fitnesses)
        if self.gen != 0:
            print(f"Average fitness over {len(self.fitnesses) + self.num_elites} instances: {avg}")
        else:
            print(f"Average fitness over {len(self.fitnesses)} instances: {avg}")

        # print top three best fit solns
        best = min(self.fitnesses)
        print(best)
        self.best_idx = self.fitnesses.index(best)
        print(f"Best solution: {self.pool.poolAsList()[self.best_idx].getSolution()}")
        # perhaps print the fitness landscape

        plt.plot(self.fitnesses)
        plt.axhline(y=avg, color='r', linestyle='-')
        plt.title(f"Fitness Landscape for Solutions in Generation {self.gen}")
        plt.savefig(self.path + f'Generation_{self.gen}')
        plt.close()

        return avg
        #plt.show()

    def solution_export(self):
        with open(self.path + 'results.txt', 'w') as file:
            file.write(f'Best Solultion: {self.pool.poolAsList()[self.best_idx].getSolution()} \n')
            actual = sum(self.pool.poolAsList()[self.best_idx].getSolution())
            accuracy = actual / self.k
            file.write(f'Accuracy to the true value k:{self.k} for an estimated:{actual} -> {accuracy} \n')
            file.write(f'Final generation: {self.gen}\n')
            file.write(f'Average fitness in final generation: {sum(self.fitnesses) / len(self.fitnesses)}\n')

            file.close()

    def optimal(self):
        self.trap = True

    def trapped(self):
        return self.trap


