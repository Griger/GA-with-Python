import reader as rd
import AGgeneric as AG
import numpy as np
from collections import namedtuple

genericParameters = namedtuple("genericParameters", "populationSize crossProbability mutationProbability")

np.random.seed(12345678)

parameters = genericParameters(10, 0.3, 0.1)
problemDim, distanceMtx, weightMtx = rd.readData("bur26a.dat")

AG.AG(parameters, problemDim, distanceMtx, weightMtx)
