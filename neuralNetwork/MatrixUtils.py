import random

def generateMatrix(rowSize, columnSize):
    matrix = []
    for i in range(0, rowSize):
        newRow = []
        for j in range(0, columnSize):
            newRow.append(getRandomValue())

        matrix.append(newRow)

    return matrix

# TODO: check is power function exec time > subtract ? make -0.5 else powerFunction
def getRandomValue():
    powerLevel = random.randint(1,2)
    return ((-1)**powerLevel * random.random())

def getDotProductOfMatrices(matrix, vector):
    dot = []
    if isinstance(vector, list):
        dot = getDotByVector(matrix, vector)
    else:
        dot = getDot(matrix, vector)

    return dot

def getDotByVector(matrix, vector):
    matrixLen = len(matrix[0])
    vectorLen = len(vector)

    dotLen = vectorLen if matrixLen > vectorLen else matrixLen

    dot = []

    for i in range(0, len(matrix)):
        dotElement = 0
        for j in range(0, dotLen):
            dotElement = dotElement + matrix[i][j] * vector[j]

        dot.append(dotElement)

    return dot

def getDot(matrix, vector):
    dot = []
    for row in matrix:
        dot.append(row[0]*vector)

    return dot
