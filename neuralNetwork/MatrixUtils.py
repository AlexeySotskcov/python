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
    dot = []
    for i in range(0, len(matrix)):
        dotElement = 0
        for j in range(0, len(vector)):
            dotElement = dotElement + float(matrix[i][j]) * float(vector[j][0])

        dot.append(dotElement)

    return dot

def multiplyMatrix(matrix, value):
    result = []
    for i in range(0, len(matrix)):
        if isinstance(matrix[0], list):
            result.append([])
            for j in range(0, len(matrix[0])):
                result[i].append(float(matrix[i][j])*value)
        else:
            for j in range(0, len(matrix[0])):
                result.append(float(matrix[i][j])*value)
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
            resultmatrix[i][j] = (firstMatrix[i][j]-secondMatrix[i][j])

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

def addValueToMatrix(matrix, value):
    matrixCopy = list(matrix)
    for i in range(0, len(matrix)):
        if isinstance(matrix[0], list):
            for j in range(0, len(matrix[0])):
                matrixCopy[i][j] += value
        else:
            matrixCopy[i] += value

    return matrixCopy

def multiplyMatrices(firstMatrix, secondMatrix):
    result = []
    if len(firstMatrix[0]) > 1:
        result = generateMatrixWithValue(len(firstMatrix), len(firstMatrix[0]), 0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] += (firstMatrix[i][j] * secondMatrix[j][i])
    else:
        result = generateMatrixWithValue(len(firstMatrix), 1, 0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] += (firstMatrix[i][j] * secondMatrix[i][j])



    return result

def reshape(valuesList, rows, cols):
    result = []
    valuesLen = len(valuesList)
    for i in range(rows):
        result.append([])
        for j in range(cols):
            index = i*rows + j
            value = valuesList[index] if valuesLen > index else 0
            result[i].append(float(value))

    return result

def getMaxArg(valuesList):
    if len(valuesList) == 0:
        return None
    if len(valuesList) == 1:
        return valuesList[0]
    else:
        maxNum = max(lst[1:])
        return valuesList[0] if valuesList[0] > maxNum else maxNum