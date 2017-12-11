import math

def sigmoid(a):
    return 1.0/(1.0 + math.exp(-a))


class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output


class NeuralNetWork:
    neuron = Neuron()

    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)
        return self.neuron.getOutput()


neural_network = NeuralNetWork()
trial_data = [-1.0, -2.0, 13.0]
print(neural_network.commit(trial_data))