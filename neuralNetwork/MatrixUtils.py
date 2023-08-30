import random

def generateMatrix(rowSize, columnSize):
    matrix = []
    for i in range(0, rowSize):
        newRow = []
        for j in range(0, columnSize):
            newRow.append(getRandomValue())

        matrix.append(newRow)

    return matrix

def getRandomValue():
    powerLevel = random.randint(1,2)
    return ((-1)**powerLevel * random.random())
