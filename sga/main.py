import configparser

from neuron import Neuron

if __name__ == '__main__':
    criterion_method_string = 'GENERAL'

    print("Program that simulates a single neuron using the delta rule.")

    config = configparser.ConfigParser()
    config.read("config.ini")
    config = config[criterion_method_string]
    neuron = Neuron(config)
    neuron.train(int(config['epoch_count']), float(config['target_precision']))
    neuron.print_weights()

