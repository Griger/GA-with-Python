import numpy as np

class Evaluator:
    def __init__(self, problemDim, weightMtx, distanceMtx):
        self.dMtx = distanceMtx
        self.wMtx = weightMtx
        self.dim = problemDim

    def checkScore(self, chromosome, score):
        actualScore = 0.0

        for i in range(self.dim):
            for j in range(self.dim):
                actualScore += self.wMtx[i][j] * self.dMtx[chromosome[i]][chromosome[j]]

        if (actualScore == score):
            print("The score is correct.")
        else:
            print(f"{score} is not correct for {chromosome}. The actual score is {actualScore}.")

    def mutationScore(self, currentChromosome, currentScore, i, j):
        newChromosome = np.copy(currentChromosome)
        newChromosome[i], newChromosome[j] = newChromosome[j], newChromosome[i]

        mutationScore = currentScore - sum(np.sum(self.wMtx[[i,j], :] * self.dMtx[currentChromosome[[i,j], None], currentChromosome], 1))
        mutationScore += sum(np.sum(self.wMtx[[i,j], :] * self.dMtx[newChromosome[[i,j], None], newChromosome], 1))

        idx = list(range(self.dim)) ; del(idx[i]) ; del(idx[j-1])

        mutationScore -= sum(sum(self.wMtx[idx][:,[i,j]] * self.dMtx[currentChromosome[idx, None], currentChromosome[[i,j]]]))
        mutationScore += sum(sum(self.wMtx[idx][:,[i,j]] * self.dMtx[newChromosome[idx, None], newChromosome[[i,j]]]))


        return mutationScore


    def score(self, chromosome):
        return sum(np.sum(self.wMtx * self.dMtx[chromosome[:, None], chromosome], 1))
