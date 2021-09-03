#!/usr/bin/env python3
""" 2-convolve_grayscale_padding task """
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    '''performs a convolution on grayscale images with custom padding
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
        padding is a tuple of (ph, pw)
                - ph is the padding for the height of the image
                - pw is the padding for the width of the image
    Important: the image will be padded with 0’s
    Returns: a numpy.ndarray containing the convolved images
    '''
    m, input_h, input_w = images.shape  # 50000 x 28 x 28

    kernel_h, kernel_w = kernel.shape  # 3 x 3

    ph, pw = padding[0], padding[1]  # 2 x 4

    output_h = input_h + 2 * ph - kernel_h + 1  # 28
    output_w = input_w + 2 * pw - kernel_w + 1  # 32

    output = np.zeros([m, output_h, output_w])  # 50000 x 28 x 32
    images = np.pad(images, [(0, 0),
                             (ph, ph),
                             (pw, pw)])  # 50000 x 30 x 26
    for h in range(output_h):
        for w in range(output_w):
            snap = images[:, h: h + kernel_h, w: w + kernel_w]
            output[:, h, w] = np.tensordot(snap, kernel, axes=([1, 2], [0, 1]))
    return output
