import NeuralNetwork
# import MatrixUtils
# neural network test script
inputNodes = 3
hiddenNodes = 3
outputNodes = 3
learningRate = 0.3

testNetwork = NeuralNetwork.NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)
print (testNetwork.query([1.0, 0.5, -1.5]))
