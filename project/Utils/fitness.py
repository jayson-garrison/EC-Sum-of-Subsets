
def fitness_function(solution, chromosome, k):
    """
    determines the fitness of a given solution

    better fitness is smaller

    infeasibles are punished

    @returns the fitness
    """
    totality = sum(solution)

    # determine feasibility
    if totality <= k:
        beta = 0
    else:
        beta = 1

    fit = abs(totality - k) + (k/10)*beta

    return fit