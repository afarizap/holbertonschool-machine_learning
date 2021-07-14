import numpy as np

# def np_slice(matrix, axes={}):
#     """ slices a matrix along specific axes """
#     for _ in axes.keys():
        
#     return matrix[axes[0], axes[1], axes[2]]

# mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np_slice(mat1, axes={1: (1, 3)}))

# def np_slice(matrix, axes={}):
#     """ slices a matrix along specific axes """
#     return matrix[2:]
# mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
#                  [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
#                  [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
# print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
axes={0: (2,), 2: (None, None, -2)}
print(axes.values())
