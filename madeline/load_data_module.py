from math import sqrt
from numpy import array, reshape


def convert_a_letter(array_of_chars):
    letter_array = []
    
    for line in array_of_chars:
        for character in line:
            if character == '-':
                letter_array.append(0)
            elif character == '#':
                letter_array.append(1)
    
    letter_array = normalise_letter(letter_array)
    return letter_array


def normalise_letter(letter_array):
    number_of_ones = letter_array.count(1)
    return [value / sqrt(number_of_ones) for value in letter_array]
    

def read_all_letters():
    letters_file = open("letters.txt", "r")
    line_number = 1
    current_letter = ""
    letters_array = []

    for line in letters_file:
        if line_number % 4 == 0:
            current_letter = current_letter + line
            current_letter.rstrip()
            letters_array.append(convert_a_letter(current_letter))
            current_letter = ""
            line_number = line_number + 1
        else:
            current_letter = current_letter + line
            line_number = line_number + 1      

    letters_file.close()
 
    return letters_array

