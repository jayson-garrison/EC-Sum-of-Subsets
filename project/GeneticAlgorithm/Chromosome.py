from Utils.fitness import fitness_function
from Utils.GenericChromosome import GenericChromosome
import numpy as np

class Chromosome(GenericChromosome):
    
    def __init__(self, solution, max) -> None:
        super().__init__(solution)
        # used for fast calculation of fitness (sum of all values in soln)
        self.solution = solution
        self.chrome = np.zeros(max)
        # construct a one-hot vector for the solutions for each value in the soln
        for number in solution:
            self.chrome[number] = 1
        
        self.fitness = fitness_function(self.solution, self.chrome)

    def getFitness(self):
        return self.fitness