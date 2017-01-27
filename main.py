import reader as rd
import GAgeneric as AG
import GAlamarck as AGL
import GAbalwinian as AGB
import numpy as np
from collections import namedtuple
import time
import evaluator as ev

def printSol(file):
    sol = np.load(file)
    print("Score:", sol["score"])
    print("Permutation:")
    print(' '.join(map(str, sol["chromosome"])))


genericParameters = namedtuple("genericParameters", "populationSize crossProbability mutationProbability")


np.random.seed(12345678)

parameters = genericParameters(100, 0.5, 0.02)
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")

ag = AG.AG(problemDim, weightMtx, distanceMtx)
agl = AGL.AGL(problemDim, weightMtx, distanceMtx)
agb = AGB.AGB(problemDim, weightMtx, distanceMtx)

print(agl.AGL(parameters))

# for cp in [0.1, 0.5, 0.7]:
#     for mp in [0, 0.01, 0.05, 0.1]:
#         parameters = genericParameters(100, cp, mp)
#         agl.AGL(parameters)

#printSol("resultsLamarck20Best/PS100CP0.5MP0.02iter228score44804670time1104.5440604686737.npy")
