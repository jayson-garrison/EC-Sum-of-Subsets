from Utils.fitness import fitness_function
from Utils.GenericChromosome import GenericChromosome
import numpy as np

class Chromosome(GenericChromosome):
    
    def __init__(self, key, k, solution = list(), chrome = np.zeros(0)) -> None:
        super().__init__(solution)
        # used for fast calculation of fitness (sum of all values in soln)
        self.solution = solution
        self.k = k
        self.key = key # the key used to determine the values in the chromosome

        if chrome.size != 0:
            self.chrome = chrome
            self.updateSolution()
        else:
            self.chrome = np.zeros(len(self.key))
            #print(self.chrome)
            # construct a one-hot vector for the solutions for each value in the soln
            for value in solution:
                #if value in solution:
                i = solution.index(value)
                self.chrome[i] = 1
        
        self.fitness = fitness_function(self.solution, self.chrome, self.k)

    def getFitness(self):
        """
        @returns the fitness of the chromosome
        """
        return self.fitness

    def vectorSize(self):
        """
        @returns the size of the chromosome one-hot vector
        """
        return self.chrome.size

    def updateSolution(self):
        """
        updates the solution based on the chromosome
        """
        self.solution.clear()
        for idx in range(self.chrome.size - 1):
            if self.chrome[idx] == 1:
                self.solution.append(self.key[idx])
                
        self.fitness = fitness_function(self.solution, self.chrome, self.k)
    
    def getChromosome(self):
        """
        @returns the chromosome (is a numpy array)
        """
        return self.chrome
    
    def getSolution(self):
        return self.solution