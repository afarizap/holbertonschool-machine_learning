#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

Deep = __import__('27-deep_neural_network').DeepNeuralNetwork
one_hot_encode = __import__('24-one_hot_encode').one_hot_encode
one_hot_decode = __import__('25-one_hot_decode').one_hot_decode

lib= np.load('../data/MNIST.npz')
X_train_3D = lib['X_train']
Y_train = lib['Y_train']
X_valid_3D = lib['X_valid']
Y_valid = lib['Y_valid']
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1)).T
X_valid = X_valid_3D.reshape((X_valid_3D.shape[0], -1)).T
Y_train_one_hot = one_hot_encode(Y_train, 10)
Y_valid_one_hot = one_hot_encode(Y_valid, 10)

deep = Deep.load('27-saved.pkl')
A_one_hot, cost = deep.train(X_train, Y_train_one_hot, iterations=100,
                             step=10, graph=False)
A = one_hot_decode(A_one_hot)
accuracy = np.sum(Y_train == A) / Y_train.shape[0] * 100
print("Train cost:", cost)
print("Train accuracy: {}%".format(accuracy))

A_one_hot, cost = deep.evaluate(X_valid, Y_valid_one_hot)
A = one_hot_decode(A_one_hot)
accuracy = np.sum(Y_valid == A) / Y_valid.shape[0] * 100
print("Validation cost:", cost)
print("Validation accuracy: {}%".format(accuracy))

deep.save('27-output')

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    fig.add_subplot(10, 10, i + 1)
    plt.imshow(X_valid_3D[i])
    plt.title(A[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
ubuntu@alexa-ml:~$ ./27-main.py
Cost after 0 iterations: 0.4388904112857044
Cost after 10 iterations: 0.4377828804163359
Cost after 20 iterations: 0.43668839872612714
Cost after 30 iterations: 0.43560674736059446
Cost after 40 iterations: 0.43453771176806555
Cost after 50 iterations: 0.4334810815993252
Cost after 60 iterations: 0.43243665061046205
Cost after 70 iterations: 0.4314042165687683
Cost after 80 iterations: 0.4303835811615513
Cost after 90 iterations: 0.4293745499077264
Cost after 100 iterations: 0.42837693207206473
Train cost: 0.42837693207206473
Train accuracy: 88.442%
Validation cost: 0.39517557351173044
Validation accuracy: 89.64%
