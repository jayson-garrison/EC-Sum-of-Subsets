
from Utils.GenericGA import GenericGA
import random as rand

from project.GeneticAlgorithm.Pool import Pool
from project.GeneticAlgorithm.Chromosome import Chromosome

class GeneticAlgorithm(GenericGA):

    def __init__(self, pool, k, upper):
        """
        init the Genetic Algorithm

        @param pool -> the pool of solutions, is a list of lists
        @param k -> desired sum for all elements in any subset to add up to be leq than
        @param upper -> the highest value in the whole set
        """
        super().__init__()
        # desired k
        self.k = k
        # init the pool given a read csv
        self.pool = Pool()
        # create chromosomes
        for soln in pool:
            self.pool.add( Chromosome(soln, upper, self.k) )
        

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
            for chrome in self.pool.poolAsList():
                total_fitness = 0
                parent_set = list()

                # determine total cumulative fitness of all chromosomes
                total_fitness = sum(self.pool.poolAsList())

                selection_probabilities = list()
                for soln_int in range(self.pool.size):
                    selection_probabilities.append(self.pool.get(soln_int).getFitness()/total_fitness)

                parents = (rand.choices(self.pool.poolAsList(), weights=selection_probabilities),\
                        rand.choices(self.pool.poolAsList(), weights=selection_probabilities) )

                parent_set.append(parents)

            return parent_set

        elif selection == 'r':
            pass
        elif selection == 't':
            pass
        else:
            print("error: invalid selection method")    


    def crossover(parents, technique):
        return super().crossover(parents, technique)

    def mutation(rate):
        return super().mutation()
