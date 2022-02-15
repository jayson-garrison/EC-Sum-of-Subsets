from Utils.fitness import fitness_function
from Utils.GenericChromosome import GenericChromosome

class Chromosome(GenericChromosome):
    
    def __init__(self, solution) -> None:
        super().__init__(solution)
        self.fitness = fitness_function(self.chrome)

    def getFitness(self):
        return self.fitness