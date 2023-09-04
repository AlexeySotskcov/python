import math
import numpy


import MatrixUtils


class NeuralNetwork:
    # W incoming hidden = hiddenNodes x inputNodes (cause of matrix multiply: row to column)
    # [A] x [B] - A (row length), B (column length)
    # cause of this, first matrix build by rule: hiddenNodes x inputNodes
    # other matrixes are build by rule:
    # outputNodes x hiddenNodes
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes
        # learning rate
        self.learningRate = learningRate
        # activation function, use sigmoid
        self.sigmoid = lambda x: 1 / (1 + math.exp(-x))

        # generate matrixes with weight coefficients
        self.inputToHiddenLayerMatrix = MatrixUtils.generateMatrix(self.hiddenNodes, self.inputNodes)
        self.hiddenToOutputLayerMatrix = MatrixUtils.generateMatrix(self.outputNodes, self.hiddenNodes)
        pass

    def train(self, inputSignals, targetSignals):
        hiddenInputs = MatrixUtils.getDotProductOfMatrices(self.inputToHiddenLayerMatrix, MatrixUtils.transposeMatrix(inputSignals))
        hiddenOuputs = []
        for hi in hiddenInputs:
            hiddenOuputs.append([self.sigmoid(hi)])

        finalInputs = MatrixUtils.getDotProductOfMatrices(self.hiddenToOutputLayerMatrix, MatrixUtils.transposeMatrix(hiddenOuputs))
        finalOutputs = []

        for fi in finalInputs:
            finalOutputs.append([self.sigmoid(fi)])


        print('finalOutputs')
        print(finalOutputs)
        print('targetSignals')
        print(targetSignals)
        transposedTargetSignals = MatrixUtils.transposeMatrix([targetSignals])
        print('transposedTargetSignals')
        print(transposedTargetSignals)
        outputErrors = MatrixUtils.subtractMatrices(transposedTargetSignals, finalOutputs)
        print('outputErrors')
        print(outputErrors)



        hiddenErrorsList = MatrixUtils.getDotProductOfMatrices(MatrixUtils.transposeMatrix(self.hiddenToOutputLayerMatrix), outputErrors)
        hiddenErrors = []
        for he in hiddenErrorsList:
            hiddenErrors.append([he])

        # weigth k of matrices
        hiddenErrorToOutputs = MatrixUtils.multiplyMatrices(outputErrors, finalOutputs)
        deltaSigmaHidden = MatrixUtils.addValueToMatrix(finalOutputs, -1)
        deltaErrorsHidden = MatrixUtils.multiplyMatrices(hiddenErrorToOutputs, deltaSigmaHidden)
        adjustmentHiddenMatrix = MatrixUtils.getDotProductOfMatrices(deltaErrorsHidden, MatrixUtils.transposeMatrix(hiddenOuputs))
        print('adjustmentHiddenMatrix')
        print(adjustmentHiddenMatrix)
        print('self.hiddenToOutputLayerMatrix')
        print(self.hiddenToOutputLayerMatrix)
        self.hiddenToOutputLayerMatrix = MatrixUtils.addMatrices(self.hiddenToOutputLayerMatrix, adjustmentHiddenMatrix)


        # weigth k of matrices
        print('hiddenErrors')
        print(hiddenErrors)
        print('hiddenOuputs')
        print(hiddenOuputs)

        hiddenOutputsToErrors = MatrixUtils.multiplyMatrices(hiddenErrors, hiddenOuputs)
        # (1-sigmoid)
        deltaSigma = MatrixUtils.addValueToMatrix(hiddenOuputs, -1)
        deltaErrors = MatrixUtils.multiplyMatrices(hiddenOutputsToErrors, deltaSigma)
        adjustmentMatrix = MatrixUtils.getDotProductOfMatrices(deltaErrors, MatrixUtils.transposeMatrix(inputSignals))
        self.inputToHiddenLayerMatrix = MatrixUtils.multiplyMatrix(
            MatrixUtils.addMatrices(self.inputToHiddenLayerMatrix, adjustmentMatrix),
            self.learningRate
        )
        # result adjustment weight
        adjustmentMatrix = MatrixUtils.getDotProductOfMatrices(deltaErrors, MatrixUtils.transposeMatrix(inputSignals))

        self.hiddenToOutputLayerMatrix = MatrixUtils.multiplyMatrix(
            MatrixUtils.addMatrices(self.hiddenToOutputLayerMatrix, adjustmentMatrix),
            self.learningRate
        )

        pass


    def query(self, inputSignals):
        hiddenInputs = MatrixUtils.getDotProductOfMatrices(self.inputToHiddenLayerMatrix, MatrixUtils.transposeMatrix(inputSignals))
        hiddenOuputs = []
        for hi in hiddenInputs:
            hiddenOuputs.append(self.sigmoid(hi))

        finalInputs = MatrixUtils.getDotProductOfMatrices(self.hiddenToOutputLayerMatrix, MatrixUtils.transposeMatrix(hiddenOuputs))
        finalOutputs = []

        for fi in finalInputs:
            finalOutputs.append([self.sigmoid(fi)])

        return finalOutputs