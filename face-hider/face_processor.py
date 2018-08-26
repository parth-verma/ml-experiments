import numpy as np
import cv2


def generate_average_filter(size):
    return np.ones((size, size), np.float32) / size ** 2


def pixelate(image, kernel_size=20):
    kernel = generate_average_filter(kernel_size)
    img_new = cv2.filter2D(image, -1, kernel)

    return img_new
