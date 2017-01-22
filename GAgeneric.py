import numpy as np
from math import *
import evaluator as ev

#Implementation of a generic genetic algorithm

class AG:
    def __init__(self, problemDim, weightMtx, distanceMtx):
        self.evaluator = ev.Evaluator(problemDim, weightMtx, distanceMtx)
        self.dim = problemDim

    def cross(self, parent1, parent2, i, j):
        if i > j:
            i,j = j,i

        n = self.dim

        idx = list(range(j+1,n)) + list(range(0, i))
        child1, child2 = parent1.copy(), parent2.copy()

        child1["chromosome"][idx] = [elem for elem in parent2["chromosome"] if elem not in parent1["chromosome"][i:j+1]]
        child2["chromosome"][idx] = [elem for elem in parent1["chromosome"] if elem not in parent2["chromosome"][i:j+1]]

        child1["score"], child2["score"] = self.evaluator.score(child1["chromosome"]), self.evaluator.score(child2["chromosome"])

        return child1, child2

    def mutate(self, individual, i, j):
        if i > j:
            i,j = j,i

        individual["score"] = self.evaluator.mutationScore(individual["chromosome"], individual["score"], i, j)
        individual["chromosome"][i], individual["chromosome"][j] = individual["chromosome"][j], individual["chromosome"][i]

    def AG (self, parameters):
        print(f"Running AG over a {self.dim}-dimension problem")

        n = self.dim
        popSize = parameters.populationSize
        crossProb = parameters.crossProbability
        mutationProb = parameters.mutationProbability

        nCrosses = ceil(popSize/2.0 * crossProb)
        nMutations = ceil(popSize * n * mutationProb)

        sizeChromosomeString = str(n) + 'int'
        dataType = np.dtype([('chromosome', sizeChromosomeString), ('score', np.float32)])

        #create initial poblation
        parent = np.zeros(popSize, dtype = dataType)

        for individual in parent:
            individual["chromosome"] = np.random.permutation(n)
            individual["score"] = self.evaluator.score(individual["chromosome"])

        parent.sort(order = "score", kind = 'mergesort')

        for i in range(1):
            if (i % 10 == 0):
                print(f"Generación {i}")
            #selection by binary tournament
            selectedParentIdx = np.empty(popSize, dtype = np.int32)

            for idx in range(popSize):
                selectedParentIdx[idx] = np.random.randint(low = 0, high = np.random.randint(1, popSize))

            selectedPairs = zip(selectedParentIdx[0:2*nCrosses:2], selectedParentIdx[1:2*nCrosses:2])

            #cross
            children = np.zeros(popSize, dtype = dataType)
            crossPoints = np.random.randint(n, size = 2*nCrosses)

            for pair, idx1, idx2 in zip(selectedPairs, range(0,2*nCrosses,2), range(1,2*nCrosses,2)):
                children[idx1], children[idx2] = self.cross(parent[pair[0]], parent[pair[1]], crossPoints[idx1], crossPoints[idx2])

            children[2*nCrosses:] = parent[selectedParentIdx[2*nCrosses:]].copy()

            #mutation
            mutantChildrenIdx = np.random.randint(popSize, size = nMutations)
            mutantGenes = np.random.randint(n, size = 2*nMutations)

            for idx, genIdx in zip(mutantChildrenIdx, range(nMutations)):
                self.mutate(children[idx], mutantGenes[2*genIdx], mutantGenes[2*genIdx+1])

            #replacement with elitism
            children.sort(order = "score", kind = 'mergesort')

            if children["score"][0] > parent["score"][0]:
                children[-1] = parent[0]

            parent = children

            parent.sort(order = "score", kind = 'mergesort')

        return parent[0]["chromosome"], parent[0]["score"]
