#!/usr/bin/env python3
""" 1-convolve_grayscale_same task """
import numpy as np


def convolve_grayscale_same(images, kernel):
    '''performs a same convolution on grayscale images
    Args:
        images is a numpy.ndarray with shape (m, h, w) containing multiple
               grayscale images
               - m is the number of images
               - h is the height in pixels of the images
               - w is the width in pixels of the images
        kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
               for the convolution
               - kh is the height of the kernel
               - kw is the width of the kernel
    Important: if necessary, the image is padded with 0’s
    Returns: a numpy.ndarray containing the convolved images
    '''
    m, input_h, input_w = images.shape  # 50000 x 28 x 28

    kernel_h, kernel_w = kernel.shape  # 3 x 3

    output = np.zeros([m, input_h, input_w])  # 5000 x 28 x 28
    images = np.pad(images, [(0, 0),
                             (kernel_h//2, kernel_h//2),
                             (kernel_w//2, kernel_w//2)])

    for h in range(input_h):
        for w in range(input_w):
            snap = images[:, h: h + kernel_h, w: w + kernel_w]
            output[:, h, w] = np.tensordot(snap, kernel, axes=([1, 2], [0, 1]))
    return output
