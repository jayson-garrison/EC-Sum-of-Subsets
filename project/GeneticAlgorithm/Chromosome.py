from Utils.fitness import fitness_function
from Utils.GenericChromosome import GenericChromosome
import numpy as np

class Chromosome(GenericChromosome):
    
    def __init__(self, range_, k, solution = list(), chrome = None) -> None:
        super().__init__(solution)
        # used for fast calculation of fitness (sum of all values in soln)
        self.solution = solution
        self.k = k

        if chrome != None:
            self.updateSolution()
        else:
            self.chrome = np.zeros(range_[1] - range_[0])
        
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
        self.solution.clear()
        for idx in range(self.vectorSize() - 1):
            if self.chrome[idx] == 1:
                self.solution.add(idx + 1)
    
    def getChromosome(self):
        """
        @returns the chromosome (is a numpy array)
        """
        return self.chrome