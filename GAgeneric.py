import numpy as np
from math import *
import evaluator as ev

#Implementation of a generic genetic algorithm

class AG:
    def __init__(self, problemDim, weightMtx, distanceMtx):
        self.evaluator = ev.Evaluator(problemDim, weightMtx, distanceMtx)
        self.dim = problemDim
        
    def cross(self, parent1, parent2, i, j):
        n = self.dim

        idx = list(range(j+1,n)) + list(range(0, i)) 
        child1, child2 = parent1.copy(), parent2.copy()

        child1["chromosome"][idx] = [elem for elem in parent2["chromosome"] if elem not in parent1["chromosome"][i:j+1]]
        child2["chromosome"][idx] = [elem for elem in parent1["chromosome"] if elem not in parent2["chromosome"][i:j+1]]

        child1["score"], child2["score"] = self.evaluator.score(child1["chromosome"]), self.evaluator.score(child2["chromosome"])

        return child1, child2

        

    def mutate(self, individual, i, j):
        individual["score"] = self.evaluator.mutationScore(individual["chromosome"], individual["score"], i, j)
        individual["chromosome"][i], individual["chromosome"][j] = individual["chromosome"][j], individual["chromosome"][i]
    


    def AG (self, parameters):
        print(f"Running AG over a {self.dim}-dimension problem")

        n = self.dim
        popSize = parameters.populationSize
        crossProb = parameters.crossProbability
        mutationProb = parameters.mutationProbability

        sizeChromosomeString = str(n) + 'int'
        dataType = np.dtype([('chromosome', sizeChromosomeString), ('score', np.float32)])

        parent = np.zeros(popSize, dtype = dataType)

        for individual in parent:
            individual["chromosome"] = np.random.permutation(n)
            individual["score"] = self.evaluator.score(individual["chromosome"])

        print(parent["chromosome"])
        print(parent["score"])

        
        print("Los padres antes")
        print(parent[0])
        print(parent[1])
        
        child1, child2 = self.cross(parent[0], parent[1],1, 1)

        print("Los hijos")
        print(child1)
        print(child2)

        print("Los padres despuess")
        print(parent[0])
        print(parent[1])
        
          
        '''
        self.mutate(parent[0], 0, 1)
    
        print(parent[0]["chromosome"])
        print(parent[0]["score"])
        '''
        return parent[0]["chromosome"]




