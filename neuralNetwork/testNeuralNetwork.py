import NeuralNetwork
import MatrixUtils
# used for images
# 28*28 =784
# image size
inputNodes = 784
# 100 symbols available in train file
hiddenNodes = 100
# 10 number available in result file
outputNodes = 10
learningRate = 0.3

testNetwork = NeuralNetwork.NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# load train data MNIST
dataFile = open("/trainSets/train100.csv", 'r')
dataList = dataFile.readlines()
dataFile.close()

# train neeralNetwork
for record in dataList:
    allValues = record.split(',')

    # 255 - color max value, but we expect 1
    # 0.99 max value, to work with small entries - less than 1
    # 0.01 - make 1 as a max param
    scaleValue = 0.99/255
    scaledInput = MatrixUtils.addValueToMatrix(
        MatrixUtils.multiplyMatrix(allValues[1:], 0.99/255),
        0.01
    )
    inputs = MatrixUtils.reshape(scaledInput, 28, 28)
    # create target output values (all equal to 0.01 except
    # desired marker value, which is 0.99)
    targets = MatrixUtils.generateMatrixWithValue(0, 10, 0.01)

    # set desired marker value
    targets[int(allValues[0])] = 0.99

    testNetwork.train(inputs, targets)
    pass