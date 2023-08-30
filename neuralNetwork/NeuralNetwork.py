import math

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

    def train():
        pass

    def query(self, inputSignals):
        hiddenInputs = MatrixUtils.getDotProductOfMatrices(self.inputToHiddenLayerMatrix, inputSignals)
        hiddenOuputs = []
        for hi in hiddenInputs:
            hiddenOuputs.append(self.sigmoid(hi))

        finalInputs = MatrixUtils.getDotProductOfMatrices(self.hiddenToOutputLayerMatrix, hiddenOuputs)
        finalOutputs = []

        for fi in finalInputs:
            finalOutputs.append(self.sigmoid(fi))

        return finalOutputs

n = NeuralNetwork(3,3,3,0.3)
n.query([1.0, 0.5, -1.5])