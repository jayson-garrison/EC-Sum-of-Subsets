import numpy as np
from Utils.GenericGA import GenericGA
import random as rand

from GeneticAlgorithm.Pool import Pool
from GeneticAlgorithm.Chromosome import Chromosome

class GeneticAlgorithm(GenericGA):

    def __init__(self, init_population, num_elites, k, range_):
        """
        init the Genetic Algorithm

        @param init_population -> the initial population of solutions, is a list of lists
        @param num_elites -> the number of elites to keep in the pool each generation
        @param k -> desired sum for all elements in any subset to add up to be leq than
        @param range_ -> (a,b) where a and b are the upper and lower limits of possible values in the set
        """
        super().__init__()
        # number of elites to keep
        self.num_elites = num_elites
        # upper limit
        self.range_ = range_
        # desired k
        self.k = k
        # init the pool given a read csv
        self.pool = Pool()
        # create chromosomes
        for soln in init_population:
            #print(soln)
            self.pool.add( Chromosome(self.range_, self.k, soln) )
        

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
            print(parent_set[0])
            return parent_set

        elif selection == 'r':
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
                child = np.zeros(self.range_[1]-self.range_[0])
                for idx in range(self.range_[1]-self.range_[0]):
                    which = rand.randint(0,1)
                    if which == 0:
                        #print(type(pair[0]))
                        #print(pair[0])
                        child[idx] = pair[0].getChromosome()[idx]
                    else:
                        #print(type(pair[1]))
                        #print(pair[1])
                        child[idx] = pair[1].getChromosome()[idx]

                child_pool.append(Chromosome(self.range_, self.k, list(), child))

            return child_pool
        elif technique == 'n-pt':
            pass
        else:
            print("error: invalid crossover technique")

    def mutation(self, num_bits, rate = 0.05):
        """
        mutate each chromosome in the pool given a probability

        @param num_bits -> upon a successful mutation, the number of bits to flip in the chromosome

        @param rate -> a number between 0 and 1 for the mutation rate (.05 is common)
        """
        super().mutation()

        for chrome in self.pool.poolAsList():
            mutation_chance = rand.randint(1, 100)
            flips = set()
            # mutation sucessful
            if mutation_chance <= rate * 100:
                # generate a set of random indicies to flip
                while (len(flips) < num_bits):
                    flip_index = rand.randint(0, chrome.vectorSize() - 1)
                    while flip_index in flips:
                        flip_index = rand.randint(0, chrome.vectorSize())
                    flips.add(flip_index)
                
                for idx in flips:
                    if chrome.getChromosome()[idx] == 0:
                        chrome.getChromosome()[idx] == 1
                    else:
                        chrome.getChromosome()[idx] == 0

                # update the solution to reflect the mutated chromosome        
                chrome.updateSolution()

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
        self.fitnesses = list()
        for chrome in self.pool.poolAsList():
            self.fitnesses.append(chrome.getFitness())

        # find the elites, add them to new pool
        for _ in range(self.num_elites):
            elite_fitness = min(self.fitnesses) # min!!
            elite = self.pool.get( self.fitnesses.index(elite_fitness) )
            new_pool.add(elite)
            self.fitnesses.remove(elite_fitness)

        # can add past pools to a generations list?
        #self.pool.removeAll()
        self.pool = new_pool
    def propagate(self, selection_method, crossover_technique, n = 1, num_bits = 1, mutation_rate = 0.05 ):
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
        # select parents
        parents = self.select_parents(selection_method)
        # crossover
        childs = self.crossover(parents, crossover_technique, n)
        # generate
        self.generation(childs)
        # mutate
        self.mutation(num_bits, mutation_rate)
        # stats
        self.statistics()

    def statistics(self):
        """
        prints statistics regarding the genetic algorithm process in solving the current problem
        """
        # print average fitness in this generation
        avg = sum(self.fitnesses) / len(self.fitnesses)
        print(f"Average fitness over {len(self.fitnesses) + self.num_elites} instances: {avg}")
        # print top three best fit solns
        best = min(self.fitnesses)
        pos = self.fitnesses.index(best)
        print(f"Best solution: {self.pool.poolAsList()[pos].getSolution()}")
        # perhaps print the fitness landscape


