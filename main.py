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

parameters = genericParameters(100, 0.3, 0.1)
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")

ag = AG.AG(problemDim, weightMtx, distanceMtx)
agl = AGL.AGL(problemDim, weightMtx, distanceMtx)
agb = AGB.AGB(problemDim, weightMtx, distanceMtx)



start = time.time()
print(agl.AGL(parameters))
end = time.time()

print("Se han tardado", end-start, "segundos para una generación.")


'''
printSol("resultsLamarck20Best/PS100CP0.3MP0.1iter37score44811992.0time10933.00833106041.npy")
problemDim, weightMtx, distanceMtx = rd.readData("tai256c.dat")
evaluator = ev.Evaluator(problemDim, weightMtx, distanceMtx)

a = np.load("resultsLamarck20Best/PS100CP0.3MP0.1iter37score44811992.0time10933.00833106041.npy")

print(a)
evaluator.checkScore(a["chromosome"], a["score"])
'''
