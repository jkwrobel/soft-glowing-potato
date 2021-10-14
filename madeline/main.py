#from network_module import Network
#from layer_module import Layer
#from activation_module import Activation
from load_data_module import read_all_letters
from numpy import dot, array, reshape

if __name__ == "__main__":
    letter_array = read_all_letters()    
    letter_array = array(letter_array)
    letter_array = reshape(letter_array, (26, 1, 16))

    weights_array = read_all_letters()
    weights_array = array(weights_array)
    weights_array = weights_array.T
    weights_array = reshape(weights_array, (16, 26))

    result = dot(letter_array, weights_array)
    
    