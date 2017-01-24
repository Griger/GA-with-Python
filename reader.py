import numpy as np
def readData (file):
    f = open("data/"+file)

    #read problem dimension
    dim = int(f.readline().split()[0])

    #read first matrix
    f.readline()
    matrixLines = [f.readline().split() for i in range(dim)]
    matrix = np.asarray([[float(number) for number in line] for line in matrixLines], dtype = np.float32)

    #read second matrix
    f.readline()
    matrixLines = [f.readline().split() for i in range(dim)]

    secondMatrix = np.asarray([[float(number) for number in line] for line in matrixLines], dtype = np.float32)

    return dim, matrix, secondMatrix
