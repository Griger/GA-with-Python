import time

class Opt:
    def __init__(self, problemDim, evaluator):
        self.dim = problemDim
        self.evaluator = evaluator

    def twoOpt (self, initialIndividual):
        bestIndividual = None
        S = initialIndividual.copy()

        evaluate = self.evaluator.mutationScoreOpt

        while (S != bestIndividual):
            bestIndividual = S.copy()

            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    newScore = evaluate(S["chromosome"], S["score"], i, j)

                    if S["score"] > newScore:
                        S["chromosome"][i], S["chromosome"][j] = S["chromosome"][j], S["chromosome"][i]
                        S["score"] = newScore
                        
        print("Acabandoo un 2opt")
        return bestIndividual
