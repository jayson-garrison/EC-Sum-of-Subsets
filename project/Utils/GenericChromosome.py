
class GenericChromosome:
    """
    Generic chromosome representation
    """
    def __init__(self, solution) -> None:
        self.chrome = solution
        #self.fitness needs to be defined

    def getFitness(self):
        """
        determine and get the fitness of the chromosome

        returns:
            the fitness of the chromosome
        """
        pass # define the fitness fx