import reader as rd
import GAgeneric as AG
import numpy as np
from collections import namedtuple
import time

genericParameters = namedtuple("genericParameters", "populationSize crossProbability mutationProbability")

np.random.seed(12345678)

parameters = genericParameters(100, 0.3, 0.2)
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
B = np.array([[1,2,3,4],[10,20,30,40],[100,200,300,400],[1000,2000,3000,4000]])


ag = AG.AG(problemDim, weightMtx, distanceMtx)


start = time.time()
print(ag.AG(parameters))
end = time.time()

print(f"Se han tardado {end-start} segundos para una generación.")
