import numpy as np
import evaluator as ev
import time

def cross(parent1, parent2, i,j):
    n = len(parent1)
    
    child1 = np.copy(parent1)
    child2 = np.copy(parent2)
    idx = list(range(j+1,n)) + list(range(0, i))   
    
    child1[idx] = [elem for elem in parent2 if elem not in parent1[i:j+1]]
    child2[idx] = [elem for elem in parent1 if elem not in parent2[i:j+1]]

    return child1, child2

print("Let compute some scores!")

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[10,20,30],[100,200,300]])
evaluator = ev.Evaluator(3, A, B)
print(A)
print(B)

ind = np.array([0,1,2])
ind2 = np.array([1,0,2])

print(f"Score del cromosoma original: {evaluator.score(ind)}")
print(f"Score de la mutacion: {evaluator.score(ind2)}")
print(f"Score calculado con la factorización: {evaluator.mutationScore(ind, ind2, evaluator.score(ind), 0, 1)}")

print(f"Score calculado con la otra: {evaluator.mutationScore2(ind, evaluator.score(ind), 0, 1)}")


ind1 = np.array([0,1,2,3,4,5,6,7,8,9])
ind2 = np.array([0,2,4,6,8,1,3,5,7,9])

print(cross(ind1, ind2, 3, 6))
