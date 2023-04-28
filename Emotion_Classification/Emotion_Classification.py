import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, output_size, hidden_layers, learning_rate):
        # initialize neural network with input size, output size, number of hidden layers, and learning rate
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layers = hidden_layers
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        # initialize weights and biases for all layers
        for i in range(len(hidden_layers) + 1):
            if i == 0:
                # first layer
                self.weights.append(np.random.randn(input_size, hidden_layers[i]))
                self.biases.append(np.zeros(hidden_layers[i]))
            elif i == len(hidden_layers):
                # output layer
                self.weights.append(np.random.randn(hidden_layers[-1], output_size))
                self.biases.append(np.zeros(output_size))
            else:
                # hidden layers
                self.weights.append(np.random.randn(hidden_layers[i-1], hidden_layers[i]))
                self.biases.append(np.zeros(hidden_layers[i]))

    def sigmoid(self, x):
        # sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # derivative of sigmoid activation function
        return x * (1 - x)

    def forward(self, input):
        # feed forward the input through the network
        activations = [input]
        for i in range(len(self.weights)):
            activation = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            activation = self.sigmoid(activation)
            activations.append(activation)
        return activations

    def backpropagate(self, input, output):
        # feed forward the input and calculate activations
        activations = self.forward(input)
        # calculate error in output layer
        error = output - activations[-1]
        # calculate deltas for output layer
        deltas = [error * self.sigmoid_derivative(activations[-1])]
        # propagate error backwards through hidden layers and calculate deltas
        for i in range(len(self.weights)-1, -1, -1):
            delta = np.dot(deltas[-1], self.weights[i].T) * self.sigmoid_derivative(activations[i])
            deltas.append(delta)
        deltas.reverse()
        # update weights and biases using calculated deltas
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * np.dot(activations[i].T, deltas[i+1])
            self.biases[i] += self.learning_rate * np.sum(deltas[i+1], axis=0)

    def train(self, inputs, outputs, epochs):
        # train the network for a specified number of epochs
        for i in range(epochs):
            for j in range(len(inputs)):
                self.backpropagate(inputs[j], outputs[j])

    def predict(self, input):
        # predict output for a new input example
        activations = self.forward(input)
        return activations[-1]

# example usage
inputs = np.random.randn(100, 68) # 100 input examples with 68 landmarks
outputs = np.random.randn(100, 7) # 100 output examples with 7 emotions
nn = NeuralNetwork(input_size=68, output_size=7, hidden_layers=[50, 30], learning_rate=0.1)
nn.train(inputs, outputs, epochs=100)
prediction = nn.predict(np.random.randn(68)) # predict output for a new input example
