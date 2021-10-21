import configparser
import random
import numpy as np

from sga import SGA





if __name__ == '__main__':
    config_section = 'GENERAL'

    print("Program that simulates a single neuron using the delta rule.")

    config = configparser.ConfigParser()
    config.read("config.ini")
    config = config[config_section]
    target_precision = int(config['target_precision'])
    range_start = float(config['range_start'])
    range_end = float(config['range_end'])
    chromosome_count = int(config['chromosome_count'])
    x_digits_count = len(bin(int((range_end - range_start) * 10 ** target_precision))) - 2

    run = 0
    gen = 0


    print(x_digits_count)

    sample_x = list(np.random.randint(0, 2, x_digits_count))
    print(sample_x)
