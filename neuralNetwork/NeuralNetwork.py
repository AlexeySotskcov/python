class NeuralNetwork:
    # W incoming hidden = hiddenNodes x inputNodes (cause of matrix multiply: row to column)
    # [A] x [B] - A (row length), B (column length)
    # cause of this, first matrix build by rule: hiddenNodes x inputNodes
    # other matrixes are build by rule:
    # outputNodes x hiddenNodes
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate) -> None:
        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes
        self.learningRate = learningRate
        pass

    def train():
        pass

    def query():
        pass