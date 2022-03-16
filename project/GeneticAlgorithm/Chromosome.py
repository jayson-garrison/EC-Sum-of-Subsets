from Utils.fitness import fitness_function
from Utils.GenericChromosome import GenericChromosome
import numpy as np

class Chromosome(GenericChromosome):
    
    def __init__(self, solution, max, k) -> None:
        super().__init__(solution)
        # used for fast calculation of fitness (sum of all values in soln)
        self.solution = solution
        self.chrome = np.zeros(max)
        self.k = k

        # construct a one-hot vector for the solutions for each value in the soln
        for number in solution:
            self.chrome[number - 1] = 1
        
        self.fitness = fitness_function(self.solution, self.chrome)

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
        pass
    
    def getChromosome(self):
        """
        @returns the chromosome (is a numpy array)
        """
        return self.chrome