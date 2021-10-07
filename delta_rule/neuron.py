import numpy as np
import random as rand


class Neuron:

    def __init__(self, config):
        self.config = config
        self.weight_init_upper_bound = int(config['weight_init_upper_bound'])
        self.weight_init_lower_bound = int(config['weight_init_lower_bound'])
        self.weight_count = int(config['weight_count'])
        self.train_pattern_upper_bound = int(config['train_pattern_upper_bound'])
        self.train_pattern_lower_bound = int(config['train_pattern_lower_bound'])
        self.train_pattern_count = int(config['train_pattern_count'])
        self.training_coefficient = float(config['training_coefficient'])
        self.train_patterns = []
        self.weights = []
        for i in range(self.weight_count):
            self.train_patterns.append(np.random.uniform(self.train_pattern_lower_bound, self.train_pattern_upper_bound,
                                                         self.weight_count + 1))
            self.weights.append(rand.uniform(self.weight_init_lower_bound, self.weight_init_upper_bound))

    def train(self, epoch_count=1):
        for i in range(epoch_count):
            for train_pattern in self.train_patterns:
                current_output = self.compute_vector(train_pattern[:len(train_pattern) - 1])
                output_delta = train_pattern[-1] - current_output
                for i in range(self.weight_count):
                    self.weights[i] += self.training_coefficient * output_delta * train_pattern[i]
            print('Current error: ' + str(self.calculate_error()))

    def compute_vector(self, input_vector):
        return np.dot(input_vector, self.weights)

    def calculate_error(self):
        error_sum = 0
        for train_pattern in self.train_patterns:
            error_sum += np.square(self.compute_vector(train_pattern[:len(train_pattern) - 1]) - train_pattern[-1])
        return np.sqrt(error_sum)
