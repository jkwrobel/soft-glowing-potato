from network_module import Network
from layer_module import Layer
from activation_module import Activation
from load_data_module import read_training_data


if __name__ == "__main__":
    inputs, outputs = read_training_data()
    
    # tworzenie sieci
    network = Network()
    network.add_layer(Layer(4, 2))
    network.add_layer(Activation())
    network.add_layer(Layer(2, 4))
    network.add_layer(Activation())

    # trenowanie sieci
    network.train_network(inputs, outputs, epochs=9000, learning_rate=0.02)

    # testowanie sieci
    result = network.use_trained_network(inputs)
    print(result)

