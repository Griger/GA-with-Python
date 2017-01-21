import numpy as np
from math import *
from evaluator import score, mutationScore

'''
Implementation of a generic genetic algorithm
'''

def cross(parent1, parent2, i,j):
    n = len(parent1)
    
    child1, child2 = parent1, parent2
    idx = list(range(j+1,n)) + list(0, i)
    child1["chomosome"][idx] = set(parent2["chomosome"]) - set(parent1["chomosome"][i:j+1])
    child2["chomosome"][idx] = set(parent1["chomosome"]) - set(parent2["chomosome"][i:j+1])

    child1["score"], child2["score"] = score(child1["chomosome"]), score(child2["chomosome"])

    return child1, child2

def mutate(individual, i, j):
    individual["chromosome"][i], individual["chromosome"][j] = individual["chromosome"][j], individual["chromosome"][i]
    individual["score"] = mutationScore(individual["chromosome", i, j)


def AG (parameters, problemDim, distanceMtx, weightMtx):
    print(f"Running AG over a {problemDim}-dimension problem")

    n = problemDim
    popSize = parameters.populationSize
    crossProb = parameters.crossProbability
    mutationProb = parameters.mutationProbability

    sizeChromosomeString = str(n) + 'int'
    dataType = np.dtype([('chromosome', sizeChromosomeString), ('score', np.float32)])

    parent = np.zeros(popSize, dtype = dataType)

    for individual in parent:
        individual["chromosome"] = np.random.permutation(problemDim)
        individual["score"] = score(distanceMtx, weightMtx, individual["chromosome"])

    print(parent["chromosome"])
    print(parent["score"])
   
    print(parent[0]["chromosome"])
    return parent[0]["chromosome"]




