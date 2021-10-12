import numpy as np


# klasa odpowiedzialna za przepuszczaniu wyników z klasy Layer przez funkcje aktywacji
class Activation:
    def __init__(self):
        self.input = None
        self.output = None

    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = activation_function(self.input)
        return self.output

    def backward_propagation(self, output_error, learning_rate):
        return activation_function_der(self.input) * output_error


def activation_function(x):
    return 1 / (1 + np.exp(-x))


def activation_function_der(x):
    return activation_function(x) * (1 - activation_function(x))




