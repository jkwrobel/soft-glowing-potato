import numpy as np
import random as rand


class Neuron:

    def __init__(self, config):
        self.config = config
        self.weight_init_upper_bound = int(config['weight_init_upper_bound'])
        self.weight_init_lower_bound = int(config['weight_init_lower_bound'])
        self.weight_count = int(config['weight_count'])
        self.train_pattern_count = int(config['train_pattern_count'])
        self.training_coefficient = float(config['training_coefficient'])
        self.train_patterns = np.array(np.loadtxt(config['data_file'], dtype=float))[:self.train_pattern_count]
        self.weights = []
        for i in range(self.weight_count):
            self.weights.append(rand.uniform(self.weight_init_lower_bound, self.weight_init_upper_bound))

    def train(self, epoch_count=1, target_error=0.1):
        for i in range(epoch_count):
            if i % 5 == 0:
                print('Current epoch: ' + str(i) + ' Current error: ' + str(self.calculate_error()))
            for train_pattern in self.train_patterns:
                current_output = self.compute_vector(train_pattern[:len(train_pattern) - 1])
                output_delta = train_pattern[-1] - current_output
                for j in range(self.weight_count):
                    self.weights[j] += self.training_coefficient * output_delta * train_pattern[j]

            if self.calculate_error() <= target_error:
                print('Current epoch: ' + str(i) + ' Current error: ' + str(self.calculate_error()))
                return

    def compute_vector(self, input_vector):
        return np.dot(input_vector, self.weights)

    def calculate_error(self):
        error_sum = 0
        for train_pattern in self.train_patterns:
            error_sum += np.square(self.compute_vector(train_pattern[:len(train_pattern) - 1]) - train_pattern[-1])
        return np.sqrt(error_sum)

    def print_weights(self):
        for i in range(len(self.weights)):
            print("Weight {}: {}".format(i, self.weights[i]))
