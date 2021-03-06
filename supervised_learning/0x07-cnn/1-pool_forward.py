#!/usr/bin/env python3
""" 1-pool_forward task """
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    '''performs forward propagation over a pooling layer of a neural
    network
    Args:
        A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
               containing the output of the previous layer
            - m is the number of examples
            - h_prev is the height of the previous layer
            - w_prev is the width of the previous layer
            - c_prev is the number of channels in the previous layer
        kernel_shape is a tuple of (kh, kw) containing the size of the kernel
                     for the pooling
            - kh is the kernel height
            - kw is the kernel width
        stride is a tuple of (sh, sw) containing the strides for the
               pooling
            sh is the stride for the height
            sw is the stride for the width
        mode is a string containing either max or avg, indicating whether to
             perform maximum or average pooling, respectively
    Returns: the output of the pooling layer
    '''
    m, ih, iw, ich = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride
    ph = pw = 0

    oh = int(np.floor((ih + ph * 2 - kh) / sh) + 1)  # output matrix heght
    ow = int(np.floor((iw + pw * 2 - kw) / sw) + 1)  # output matrix width

    output = np.zeros([m, oh, ow, ich])  # convolution output

    h = 0
    for i in range(oh):
        w = 0
        for j in range(ow):
            h = i * sh
            w = j * sw
            current = A_prev[:, h: h + kh, w: w + kw, :]
            if mode == 'max':
                output[:, i, j, :] = np.amax(current, (1, 2))
            elif mode == 'avg':
                output[:, i, j, :] = np.average(current, (1, 2))

    return output
