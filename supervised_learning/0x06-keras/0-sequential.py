#!/usr/bin/env python3
""" 0-sequential task """
import tensorflow.keras as K
from tensorflow.python.keras.backend import dropout
from tensorflow.python.keras.layers.core import Dropout
from tensorflow.python.keras.regularizers import Regularizer

def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    builds a neural network with the Keras library:

    nx: is the number of input features to the network
    layers: is a list containing the number of nodes in each layer of the network
    activations: is a list containing the activation functions used for each layer of the network
    lambtha: is the L2 regularization parameter
    keep_prob: is the probability that a node will be kept for dropout
    Returns: the keras model

    """
    model = K.Sequential()
    model.add(K.Input(shape=(nx,)))
    for i in range(len(layers)):
        model.add(K.layers.Dense(units=layers[i],
                  activation=activations[i],
                  activity_regularizer=K.regularizers.L2(lambtha)))
        if i != len(layers) - 1:
            model.add(K.layers.Dropout(keep_prob))
    return model