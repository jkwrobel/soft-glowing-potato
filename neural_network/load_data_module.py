from numpy import array, reshape
from pandas import read_csv

def read_training_data():
    inputs = read_csv("dataset.csv", usecols=[0,1,2,3])
    outputs = read_csv("dataset.csv", usecols=[4,5,6,7])

    inputs = reshape(inputs.to_numpy(), (4, 1, 4))
    outputs = reshape(outputs.to_numpy(), (4, 1, 4))

    return inputs, outputs

