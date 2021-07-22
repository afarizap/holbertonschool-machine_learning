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
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = list(zip(*pca_data))
ax.scatter(x, y, z, c=labels, cmap=plt.get_cmap('plasma'))
ax.set_title("PCA of Iris Dataset")
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
plt.show()
# https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
