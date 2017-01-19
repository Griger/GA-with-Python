import numpy as np
from math import *
from evaluator import score, mutationScore

'''
Implementation of a generic genetic algorithm


def cross(firstParent, secondParent):

'''
def mutate(individual, i, j):
    individual["score"] = mutationScore(individual, i, j)
    individual["chromosome"][i], individual["chromosome"][j] = individual["chromosome"][j], individual["chromosome"][i]


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




