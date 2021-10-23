import configparser

from sga import SGA


if __name__ == '__main__':
    config_section = 'GENERAL'

    print("Program that simulates a single neuron using the delta rule.")

    config = configparser.ConfigParser()
    config.read("config.ini")
    config = config[config_section]

    alg_instance = SGA(config)

    alg_instance.do_entire_sga()
