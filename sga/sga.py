import numpy as np
import random as rand


class SGA:
    def __init__(self, config):
        self.config = config
        self.run = 0
        self.gen = 0
        self.target_precision = int(config['target_precision'])
        self.target_gen_count = int(config['target_gen_count'])
        self.range_start = float(config['range_start'])
        self.range_end = float(config['range_end'])
        self.chromosome_count = int(config['chromosome_count'])
        self.crossing_prob = float(config['crossing_prob'])
        self.mutation_prob = float(config['mutation_prob'])
        self.reproduction_prob = 1 - self.crossing_prob - self.mutation_prob
        self.x_digits_count = len(bin(int((self.range_end - self.range_start) * 10 ** self.target_precision))) - 2
        self.this_chromosomes = [None] * self.chromosome_count
        self.this_chromosomes_fitness = [None] * self.chromosome_count
        self.next_chromosomes = [None] * self.chromosome_count
        self.fittest_chromosomes = [None] * self.chromosome_count

    def do_single_run(self):
        self.create_initial_population()

        while ~self.check_stop_criteria():
            for i in range(self.chromosome_count):
                self.this_chromosomes_fitness[i] = fitness_function_bin(self.this_chromosomes[i])

            j = 0
            while j < self.chromosome_count:  # I f...... HATE python for loops
                rand_prob = rand.uniform(0, self.reproduction_prob + self.crossing_prob + self.mutation_prob)
                if rand_prob <= self.reproduction_prob:
                    print('reproduction')
                elif rand_prob <= self.reproduction_prob + self.crossing_prob:
                    print('crossing')
                    j += 1
                else:
                    print('mutation')
                j += 1;  # And give me my ++ operator back. >:C

    def check_stop_criteria(self):
        return self.gen == self.target_gen_count

    def create_initial_population(self):
        for i in range(self.chromosome_count):
            self.this_chromosomes.append(list(np.random.randint(0, 2, self.x_digits_count)))




def fitness_function_dec(x):
    return (np.e ** x * np.sin(10 * np.pi * x) + 1) / x + 5


def fitness_function_bin(x):
    return fitness_function_bin(int(x, 2))
