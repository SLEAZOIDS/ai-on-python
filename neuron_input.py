class Neuron:
    input_sum = 0.0

    def setInput(self, inp):
        self.input_sum += inp
        print(self.input_sum)


class NeuralNetWork:
    neuron = Neuron()

    def commit(self, input_data):
        for data in input_data:
            self.neuron.setInput(data)


neural_network = NeuralNetWork()
trial_data = [1.0, 2.0, 3.0]
neural_network.commit(trial_data)