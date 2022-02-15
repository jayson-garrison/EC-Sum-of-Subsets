
class GenericPool():
    """
    Generic pool object that consists of chromosomes.
    """

    def __init__(self) -> None:
        self.pool = list()

    def add(self, chromosome):
        """
        adds a chromosome to the pool

        params:
            chromosome : the chromosome to be added to the pool
        """
        self.pool.append(chromosome)

    def remove(self, chromosome):
        """
        removes a chromosome from the pool

        params:
            chromosome : the chromosome to be removed from the pool
        """
        self.pool.remove(chromosome)

    def removeAll(self):
        """
        remove all the chromosomes from the pool
        """
        self.pool.clear()

    def get(self, index):
        """
        gets the ith chromosome from the pool

        params:
            index : the index of the desired chromosome in the pool

        returns:
            the ith chromosome in the pool
        """
        return self.pool[index]

    def size(self):
        """
        returns the size of the pool
        """
        return len(self.pool)