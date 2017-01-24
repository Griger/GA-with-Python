import time

class Opt:
    def __init__(self, problemDim, evaluator):
        self.dim = problemDim
        self.evaluator = evaluator

    def twoOpt (self, initialIndividual):
        print("Ejecutando 2opt")
        bestIndividual = None
        S = initialIndividual.copy()

        evaluate = self.evaluator.mutationScoreOpt

        while (S != bestIndividual):
            start = time.time()
            bestIndividual = S.copy()
            end = time.time()
            print("Se han tardado", end-start, "segundos.")

            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    newScore = evaluate(S["chromosome"], S["score"], i, j)

                    if S["score"] > newScore:
                        S["chromosome"][i], S["chromosome"][j] = S["chromosome"][j], S["chromosome"][i]
                        S["score"] = newScore

        return bestIndividual
