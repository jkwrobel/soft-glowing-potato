import numpy as np


class Network:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def use_trained_network(self, input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    def train_network(self, given_inputs, expected_outputs, epochs, learning_rate):
        samples = len(given_inputs)

        for i in range(epochs):
            error_for_one_epoch = 0
            for j in range(samples):
                output = given_inputs[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                error = mean_square_error_der(expected_outputs[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)


def mean_square_error(expected_values, gotten_values):
    return np.mean(np.power(expected_values - gotten_values, 2))


def mean_square_error_der(expected_values, gotten_values):
    return 2 * (gotten_values - expected_values) / expected_values.size


