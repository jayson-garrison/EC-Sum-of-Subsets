#from project.GeneticAlgorithm.Chromosome import Chromosome
from Utils.GenericPool import GenericPool
#from project.GeneticAlgorithm.Chromosome import Chromosome

class Pool(GenericPool):
    """
    Is a pool of chromosomes
    """
    def __init__(self, given_population = list()) -> None:
        super().__init__()
        self.pool = list()
        if len(given_population) != 0:
            for creature in given_population:
                self.pool.append( creature )
            

    def add(self, chromosome):
        return super().add(chromosome)

    def remove(self, chromosome):
        return super().remove(chromosome)

    def removeAll(self):
        return super().removeAll()

    def get(self, index):
        return super().get(index)

    def size(self):
        return super().size()
    
    def poolAsList(self):
        return self.pool

    #def chooseRandom(self)