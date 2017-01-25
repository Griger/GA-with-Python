import reader as rd
import GAgeneric as AG
import GAlamarck as AGL
import numpy as np
from collections import namedtuple
import time

genericParameters = namedtuple("genericParameters", "populationSize crossProbability mutationProbability")

np.random.seed(12345678)

parameters = genericParameters(100, 0.3, 0.1)
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")

ag = AG.AG(problemDim, weightMtx, distanceMtx)
agl = AGL.AGL(problemDim, weightMtx, distanceMtx)


start = time.time()
print(agl.AGL(parameters))
end = time.time()

print("Se han tardado", end-start, "segundos para una generación.")
