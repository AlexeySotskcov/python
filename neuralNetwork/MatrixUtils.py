import random

def generateMatrix(rowSize, columnSize):
    matrix = []
    for i in range(0, rowSize):
        newRow = []
        for j in range(0, columnSize):
            newRow.append(getRandomValue())

        matrix.append(newRow)

    return matrix

def generateMatrixWithValue(rowSize, columnSize, value):
    matrix = []
    if rowSize == 0:
        newRow = []
        for j in range(0, columnSize):
            newRow.append(value)
        return newRow
    else:
        for i in range(0, rowSize):
            newRow = []
            for j in range(0, columnSize):
                newRow.append(value)

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
        dot = []

    return dot

def getDotByVector(matrix, vector):
    matrixLen = len(matrix[0])
    vectorLen = len(vector)

    dotLen = vectorLen if matrixLen > vectorLen else matrixLen

    dot = []

    for i in range(0, len(matrix)):
        dotElement = 0
        for j in range(0, dotLen):
            dotElement = dotElement + matrix[i][j] * vector[i][0]

        dot.append(dotElement)

    return dot

def multiplyMatrix(matrix, value):
    result = []
    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[0])):
            result[i].append(matrix[i][j]*value)

    return result

def transposeMatrix(matrix):
    matrixCopy = []
    if isinstance(matrix[0], list):
        matrixCopy = list(matrix)
    else:
        matrixCopy = [list(matrix)]

    transposedMatrix = [[matrixCopy[j][i] for j in range(len(matrixCopy))] for i in range(len(matrixCopy[0]))]

    return transposedMatrix

def subtractMatrices(firstMatrix, secondMatrix):
    m1Rows = len(firstMatrix)
    m2Rows = len(secondMatrix)
    matrixRows = m1Rows if m1Rows< m2Rows else m2Rows

    m1Cols = len(firstMatrix[0])
    m2Cols = len(secondMatrix[0])
    matrixCols = m1Cols if m1Cols < m2Cols else m2Cols

    resultmatrix = generateMatrixWithValue(matrixRows, matrixCols, 0)

    for i in range(0, len(firstMatrix)):
        for j in range(0, len(firstMatrix[0])):
            resultmatrix.append(firstMatrix[i][j]-secondMatrix[i][j])

    return resultmatrix

def addMatrices(firstMatrix, secondMatrix):
    m1Rows = len(firstMatrix)
    m2Rows = len(secondMatrix)
    matrixRows = m1Rows if m1Rows< m2Rows else m2Rows

    m1Cols = len(firstMatrix[0])
    m2Cols = len(secondMatrix[0])
    matrixCols = m1Cols if m1Cols < m2Cols else m2Cols

    resultmatrix = generateMatrixWithValue(matrixRows, matrixCols, 0)

    for i in range(0, len(firstMatrix)):
        for j in range(0, len(firstMatrix[0])):
            resultmatrix.append(firstMatrix[i][j]-secondMatrix[i][j])

    return resultmatrix

def addValueToMatrix(value, matrix):
    matrixCopy = list(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrixCopy[i][j] = matrix[i][j] + value

    return matrixCopy

def multiplyMatrices(firstMatrix, secondMatrix):
    result = generateMatrixWithValue(len(firstMatrix), len(firstMatrix[0]), 0)
    for i in range(firstMatrix):
        result.append([])
        for j in range(firstMatrix[0]):
            result[i][j] += (firstMatrix[i][j] * secondMatrix[j][i])

    return result

def reshape(valuesList, rows, cols):
    result = []
    valuesLen = len(valuesList)
    for i in range(rows):
        result.append([])
        for j in range(rows):
            index = i*rows + j
            value = valuesList[index] if valuesLen > index else 0
            result[i].append(float(value))

    return result