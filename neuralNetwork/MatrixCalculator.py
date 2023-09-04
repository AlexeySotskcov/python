import random

class MatrixCalculator:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def getMatrix(self, defaultValue = 0):
        self.matrix = MatrixCalculator.buildMatrix(self.rows, self.cols, defaultValue)
        return self.matrix

    def buildMatrix(rows, cols, value):
        matrix = []
        for i in range(0, rows):
            newRow = []
            for j in range(0, cols):
                newRow.append(float(value))

            matrix.append(newRow)
        return matrix

    def getMatrixRandomValues(self):
        self.matrix = []
        for i in range(0, self.rows):
            newRow = []
            for j in range(0, self.cols):
                newRow.append(self.getRandomValue())

            self.matrix.append(newRow)

    def getRandomValue():
        powerLevel = random.randint(1,2)
        return ((-1)**powerLevel * random.random())

    def addValue(self, value):
        valueAsMatrix = MatrixCalculator.buildMatrix(self.rows, self.cols, value)
        return MatrixCalculator.matrixAddition(self.matrix, valueAsMatrix)

    def matrixAddition(matrix1, matrix2, arg=1):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise Exception("Different matrix sizes")
        result = []
        for i in range(len(matrix1)):
            newRow = []
            for j in range(len(matrix1[i])):
                newRow.append(matrix1[i][j]+arg*matrix2[i][j])
            result.append(newRow)
        return result

    def multiplyOnValue(matrix, value):
        result = []
        for i in range(len(matrix)):
            newRow = []
            for j in range(len(matrix[i])):
                newRow.append(matrix[i][j]*value)
            result.append(newRow)
        return result

    def multiplyOnMatrix(matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise Exception("Different matrix sizes")

        result = MatrixCalculator.buildMatrix(len(matrix1),len(matrix2[0]), 0.0)

        for i in range(0, len(matrix1)):
            for j in range(0, len(matrix1[i])):
                for k in range(0, len(matrix2)):
                    result[i][j] += matrix1[i][k]*matrix2[k][j]


        return result


    def transpose(matrix):
        transposedMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        return transposedMatrix


c = MatrixCalculator(3,3)
w1 = c.getMatrix(0.1)
print(w1)
w2 = c.addValue(1)
print(w2)
w3 = MatrixCalculator.multiplyOnValue(w2,2)
print(w3)
w4 = [[1,2,3],[4,5,6],[7,8,9]]
print(w4)
w5 = MatrixCalculator.transpose(w4)
print(w5)
w6 = [[6,1,8],[12,7,4],[15,2,6]]
print(w6)
w7 = MatrixCalculator.multiplyOnMatrix(w4,w6)
print(w7)