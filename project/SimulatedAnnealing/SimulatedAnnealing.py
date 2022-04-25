from GeneticAlgorithm.Chromosome import Chromosome
import numpy as np
import random as rand

class SimulatedAnnealing:
    
    def __init__(self, k, key, initial_soln) -> None:

        self.key = key
        self.k = k
        self.soln = Chromosome(key, k, initial_soln)
        

    def perturb(self, chrome, num_bits, method='u'):

        

        if method == 'flip':

            flips = set()
            # generate a set of random indicies to flip
            while (len(flips) < num_bits):
                flip_index = rand.randint(0, chrome.vectorSize() - 1)
                while flip_index in flips:
                    flip_index = rand.randint(0, chrome.vectorSize() - 1)
                flips.add(flip_index)
            
            for idx in flips:
                if chrome.getChromosome()[idx] == 0:
                    chrome.getChromosome()[idx] = 1
                else:
                    chrome.getChromosome()[idx] = 0

            # update the solution to reflect the mutated chromosome        
            chrome.updateSolution()
            return chrome

        elif method == 'fredinc':

            # seperate ones and zeros
            ones = list()
            zeros = list()
            for idx, value in enumerate(chrome.getChromosome()):
                if value == 1:
                    ones.append(idx)
                else:
                    zeros.append(idx)

            which = rand.randint(1, 100)

            reduce = list()

            if which < 90 and len(ones) != 0:
                # force reduction
                # pick num_bits randomly

                item = rand.choice(ones)
                i = 0

                if len(ones) <= num_bits:
                    # proceed
                    for index in ones:
                        chrome.getChromosome()[index] = 0
                else:
                    while item not in reduce and i < num_bits:
                        reduce.append(item)
                        item = rand.choice(ones)
                        i += 1

                    for index in reduce:
                        chrome.getChromosome()[index] = 0
                
            else:
                # force increase

                if len(zeros) == 0:
                    pass

                item = rand.choice(zeros)
                i = 0

                if len(zeros) <= num_bits:
                    # proceed
                    for index in zeros:
                        chrome.getChromosome()[index] = 1
                else:
                    while item not in reduce and i < num_bits:
                        reduce.append(item)
                        item = rand.choice(zeros)
                        i += 1

                    for index in reduce:
                        chrome.getChromosome()[index] = 1
                
            chrome.updateSolution()
            return chrome
                    
        else:
            print('error: invalid mutation technique')
            exit()
    
    def anneal(self, dirname, perturb_params, initial_temp, iterations, alpha, beta):
        '''
        perform simulated annealing
        @param perturb_params -> a tuple of (num_bits, method)
        @param initial_temp -> the initial temperature
        @param iterations -> initial iterations for inner loop
        @param alpha -> alpha
        @param beta -> beta
        
        '''
        nb = perturb_params[0]
        meth = perturb_params[1]
        self.temp = initial_temp
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta

        self.path = f'project/SimulatedAnnealing/Visuals/{dirname}/'

        self.statistics()
        itera = 0
        while itera < 50: # what is this condition? perhaps convergence
            for _ in range(self.iterations):
                soln = list()
                for item in self.soln.getSolution():
                    soln.append(item)

                newS = Chromosome(self.key, self.k, soln)
                newS = self.perturb(newS, nb, meth)
                # print(newS.getSolution())
                # print(self.soln.getSolution())
                r = rand.random()
                phi = np.exp( (self.h(self.soln) - self.h(newS)) / self.temp)
                #print(f'r: {r} phi: {phi} r < phi')
                if ( (self.h(newS) < self.h(self.soln) or r < phi) ): # and sum(newS.getSolution()) < self.k
                    self.soln = newS
            self.statistics()
            self.temp = self.alpha * self.temp
            self.iterations = int(self.beta * self.iterations)
            itera += 1

    def h(self, chromosome):
        '''
        obtain the fitness of the solution
        '''
        return chromosome.getFitness()
    
    def statistics(self):
        s = self.soln.getSolution()
        print(f'Current solution:{s}\n')
        print(f'Current sum: {sum(s)} Compared to k: {self.k}\n')
        print(f'Convergence metric: {sum(s) / self.k}\n')

