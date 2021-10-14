import configparser

from delta_rule.neuron import Neuron

if __name__ == '__main__':
    criterion_method_string = 'GENERAL'

    print("Program that simulates a single neuron using the delta rule.")

    config = configparser.ConfigParser()
    config.read("config.ini")

    neuron = Neuron(config[criterion_method_string])
    neuron.train(200)
    neuron.print_weights()

