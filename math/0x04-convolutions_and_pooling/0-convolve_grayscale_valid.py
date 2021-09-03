#!/usr/bin/env python3
""" 0-convolve_grayscale_valid task """
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """performs a valid convolution on grayscale images
    images: is a numpy.ndarray with shape (m, h, w)
     containing multiple grayscale images
        m: is the number of images
        h: is the height in pixels of the images
        w: is the width in pixels of the images
    kernel: is a numpy.ndarray with shape (kh, kw) containing the kernel
     for the convolution
        kh: is the height of the kernel
        kw: is the width of the kernel
    Returns: a numpy.ndarray containing the convolved images
    """
    m, input_h, input_w = images.shape  # 50000 x 28 x 28

    kernel_h, kernel_w = kernel.shape  # 3 x 3

    output_h = input_h - kernel_h + 1  # 26
    output_w = input_w - kernel_w + 1  # 26

    output = np.zeros([m, output_h, output_w])  # 5000 x 26 x 26

    for h in range(output_h):
        for w in range(output_w):
            snap = images[:, h: h + kernel_h, w: w + kernel_w]
            output[:, h, w] = np.tensordot(snap, kernel, axes=([1, 2], [0, 1]))
    return output
