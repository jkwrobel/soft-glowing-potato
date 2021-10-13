#from network_module import Network
#from layer_module import Layer
#from activation_module import Activation
from load_data_module import read_all_letters

if __name__ == "__main__":
    letter_array = read_all_letters()

    for character in letter_array:
        print(character)