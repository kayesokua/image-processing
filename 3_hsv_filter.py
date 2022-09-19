import matplotlib.pyplot as plt
from skimage import data, io, img_as_float, exposure
from skimage.color import rgb2hsv, rgb2lab, lab2lch
from skimage.io import imread
import numpy as np

tree_roots = imread('./sample/tree-roots-resized.jpg')
crack = imread('./sample/crack-20220918204533.jpg')

def rgb_to_hsv(image):
    return rgb2hsv(image)

def rgb_hsv_comparison(image):
    image_hsv = rgb_to_hsv(image)
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()
    ax[0].imshow(image)
    ax[0].set_title("Original")
    ax[1].imshow(image_hsv)
    ax[1].set_title("HSV")
    fig.tight_layout()
    print("Hue:",image_hsv[:, :, 0])
    print("Sat:",image_hsv[:, :, 1])
    print("Val:",image_hsv[:, :, 2])
    plt.show()


rgb_hsv_comparison(tree_roots)