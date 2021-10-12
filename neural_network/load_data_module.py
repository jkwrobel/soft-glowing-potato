import numpy as np
from numpy.core.records import array
import pandas as pd


def convert_a_letter(array_of_chars):
    letter_array = []
    
    print(array_of_chars)
    for line in array_of_chars:
        for character in line:
            if character == '-':
                letter_array.append(0)
            elif character == '#':
                letter_array.append(1)
    
    return letter_array

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

