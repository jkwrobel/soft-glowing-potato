import numpy as np
import random as rand
from random import randint


class SGA:
    def __init__(self, config):
        # general config
        self.config = config
        self.target_precision = int(config['target_precision'])
        self.range_start = float(config['range_start'])
        self.range_end = float(config['range_end'])
        self.chromosome_count = int(config['chromosome_count'])
        self.crossing_prob = float(config['crossing_prob'])
        self.mutation_prob = float(config['mutation_prob'])
        self.reproduction_prob = 1 - self.crossing_prob - self.mutation_prob

        # SGA memory
        self.run = 0
        self.gen = 0
        self.x_digits_count = len(bin(int((self.range_end - self.range_start) * 10 ** self.target_precision))) - 2
        self.this_chromosomes = [[] for _ in range(self.chromosome_count)]
        self.this_chromosomes_fitness = [-1.0] * self.chromosome_count
        self.next_chromosomes = [[] for _ in range(self.chromosome_count)]

        # roulette selection method
        self.roulette_selection_initiated = False
        self.chromosome_selection_probability = [-1.0] * self.chromosome_count

        # stop criteria
        self.consecutive_pop_to_measure = int(config['consecutive_pop_to_measure'])
        self.consecutive_pop_minimum_change_threshold = float(config['consecutive_pop_minimum_change_threshold'])
        self.target_gen_count = int(config['target_gen_count'])
        self.former_population_avg_ff = []

    def do_single_run(self):
        self.create_initial_population()

        while self.gen == 1 or not self.check_stop_criteria():
            for i in range(self.chromosome_count):
                self.this_chromosomes_fitness[i] = self.fitness_function_bin(self.this_chromosomes[i])

            j = 0
            while j < self.chromosome_count:  # I f...... HATE python for loops
                rand_prob = rand.uniform(0, self.reproduction_prob + self.crossing_prob + self.mutation_prob)
                if rand_prob <= self.reproduction_prob:  # reproduction
                    chosen_chromosome = self.select_chromosome()
                    self.next_chromosomes[j] = list(self.this_chromosomes[chosen_chromosome])
                elif rand_prob <= self.reproduction_prob + self.crossing_prob:  # crossing
                    if j + 1 >= self.chromosome_count:
                        continue
                    chosen_chromosome_1 = self.select_chromosome()
                    chosen_chromosome_2 = self.select_chromosome(chosen_chromosome_1)
                    mixed_chrom_1, mixed_chrom_2 = self.cross_two_chromosomes(chosen_chromosome_1, chosen_chromosome_2)
                    self.next_chromosomes[j] = list(mixed_chrom_1)
                    self.next_chromosomes[j + 1] = list(mixed_chrom_2)
                    j += 1
                else:  # mutation
                    mutated_chrom = self.mutate_chromosome(self.select_chromosome())
                    self.next_chromosomes[j] = mutated_chrom
                j += 1;  # And give me my ++ operator back. >:C

            print("Generation: " + str(self.gen))
            fittest_id = np.argmax(self.this_chromosomes_fitness)
            print("Fittest id: " + str(fittest_id))
            fittest_chrom = self.this_chromosomes[fittest_id]
            print("Fittest chromosome bin: " + str(fittest_chrom))
            print("Fittest chromosome dec: " + str(int(''.join(map(str, fittest_chrom)), 2) / 2**self.x_digits_count))
            print("Fittest chromosome dec: " + str(int(''.join(map(str, fittest_chrom)), 2) / 2**self.x_digits_count * (self.range_end - self.range_start) + self.range_start))
            print("Fittest chrom ff: " + str(self.fitness_function_bin(fittest_chrom)))

            self.this_chromosomes = self.next_chromosomes
            self.next_chromosomes = [[] for _ in range(self.chromosome_count)]
            self.roulette_selection_initiated = False
            self.gen += 1

    def check_stop_criteria(self):
        gen_count_stop = self.gen == self.target_gen_count

        average_value_stop_criteria = False
        curr_average = sum(self.this_chromosomes_fitness) / self.chromosome_count
        if len(self.former_population_avg_ff) < self.consecutive_pop_to_measure:
            average_value_stop_criteria = False
        else:
            average_value_stop_criteria = True
            for i in self.former_population_avg_ff[-self.consecutive_pop_to_measure:]:
                if abs(curr_average - i) > self.consecutive_pop_minimum_change_threshold:
                    average_value_stop_criteria = False
                    break
        self.former_population_avg_ff.append(curr_average)

        return gen_count_stop or average_value_stop_criteria

    def create_initial_population(self):
        for i in range(self.chromosome_count):
            self.this_chromosomes[i] = (list(np.random.randint(0, 2, self.x_digits_count)))

    def init_select_chromosome(self):
        self.roulette_selection_initiated = True
        total_fitness = sum(self.this_chromosomes_fitness)
        for i in range(self.chromosome_count):
            self.chromosome_selection_probability[i] = self.this_chromosomes_fitness[i] / total_fitness

    def select_chromosome(self, avoid=-1):
        choice = -1
        if not self.roulette_selection_initiated:
            self.init_select_chromosome()
        while choice == -1 or choice == avoid:
            rand_prob = rand.uniform(0, self.reproduction_prob + self.crossing_prob + self.mutation_prob)
            for i in range(self.chromosome_count):
                if rand_prob < self.chromosome_selection_probability[i]:
                    choice = i
                    break
                rand_prob -= self.chromosome_selection_probability[i]
        return choice

    def cross_two_chromosomes(self, chromosome_1_id, chromosome_2_id):
        chromosome_1 = list(self.this_chromosomes[chromosome_1_id])
        chromosome_2 = list(self.this_chromosomes[chromosome_2_id])
        split_index = randint(1, self.x_digits_count - 1)
        chromosome_1_l = chromosome_1[:split_index]
        chromosome_1_r = chromosome_1[split_index:]
        chromosome_2_l = chromosome_2[:split_index]
        chromosome_2_r = chromosome_2[split_index:]
        return chromosome_1_l + chromosome_2_r, chromosome_2_l + chromosome_1_r

    def mutate_chromosome(self, chromosome_id):
        chromosome = list(self.this_chromosomes[chromosome_id])
        mutate_index = randint(0, self.x_digits_count - 1)
        chromosome[mutate_index] = (chromosome[mutate_index] + 1) % 2
        return chromosome

    def fitness_function_bin(self, x):
        return fitness_function_dec(int(''.join(map(str, x)), 2) / 2**self.x_digits_count * (self.range_end - self.range_start) + self.range_start)


def fitness_function_dec(x):
    return (np.e ** x * np.sin(10 * np.pi * x) + 1) / x + 5


