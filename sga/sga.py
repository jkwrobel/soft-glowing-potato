import numpy as np
import random as rand


class SGA:
    def __init__(self, config):
        self.config = config
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

