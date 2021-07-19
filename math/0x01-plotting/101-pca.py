#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
"""Principle Component Analysis (PCA)"""


lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
u, s, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# your code here
plt.title("PCA of Iris Dataset")
fig = plt.figure()
ax3d = fig.add_subplot(111, projection='3d')

plt.show()
