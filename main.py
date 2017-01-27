import reader as rd
import GAgeneric as AG
import GAlamarck as AGL
import GAbalwinian as AGB
import GAlamarckAux as AGLAux
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
problemDim, weightMtx, distanceMtx = rd.readData("tai60a.dat")

ag = AG.AG(problemDim, weightMtx, distanceMtx)
agl = AGLAux.AGL(problemDim, weightMtx, distanceMtx)
agb = AGB.AGB(problemDim, weightMtx, distanceMtx)


for cp in [0.1, 0.5, 0.7]:
    for mp in [0, 0.01, 0.05, 0.1]:
        parameters = genericParameters(100, cp, mp)
        agl.AGL(parameters)

# start = time.time()
# print(agl.AGL(parameters))
# end = time.time()

'''


print("Se han tardado", end-start, "segundos para una generación.")
printSol("resultsLamarck20Best/PS100CP0.3MP0.1iter37score44811992.0time10933.00833106041.npy")
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")
evaluator = ev.Evaluator(problemDim, weightMtx, distanceMtx)

a = np.load("resultsLamarck20Best/PS100CP0.3MP0.1iter37score44811992.0time10933.00833106041.npy")

print(a)
evaluator.checkScore(a["chromosome"], a["score"])
'''
