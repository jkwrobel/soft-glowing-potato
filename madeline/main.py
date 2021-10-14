#from network_module import Network
#from layer_module import Layer
#from activation_module import Activation
from load_data_module import read_all_letters
from numpy import dot, array, reshape, where, amax

if __name__ == "__main__":
    letter_array = read_all_letters()    
    letter_array = array(letter_array)
    letter_array = reshape(letter_array, (26, 1, 16))

    weights_array = read_all_letters()
    weights_array = array(weights_array)
    weights_array = weights_array.T
    weights_array = reshape(weights_array, (16, 26))

    result = dot(letter_array, weights_array)

    position_meaning = open('outputs.txt')
    output_lines = position_meaning.readlines()

    files_with_results = open("results.txt", "a")
    for output in result:
        for output_letter in output:
            for i in range(26):
                files_with_results.write("The value for letter " + str(output_lines[i]).rstrip() + " equals to: " + str(output_letter[i]) + "\n")
            result = where(output_letter == amax(output_letter))
            letter_index = result[0][0]
            files_with_results.write("=> NETWORK HAS RECOGNISED LETTER " + str(output_lines[letter_index]) + "\n\n")
    
    