#!/usr/bin/env python3
""" 0-create_placeholders task  (WORKS FOR TF 2.6)"""
import tensorflow as tf
tf.compat.v1.disable_eager_execution()


def create_placeholders(nx, classes):
    """
    args:
        nx: the number of feature columns in our data
        classes: the number of classes in our classifier
    Returns: placeholders named x and y, respectively
        x is the placeholder for the input data to the neural network
        y is the placeholder for the one-hot labels for the input data
    """
    x = tf.compat.v1.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.compat.v1.placeholder(tf.float32, shape=(None, classes), name='y')
    return x, y
