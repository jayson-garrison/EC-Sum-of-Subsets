from project.Utils.GenericPool import GenericPool

class Pool(GenericPool):
    """
    Is a pool of chromosomes
    """
    def __init__(self) -> None:
        super().__init__()

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