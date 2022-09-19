from skimage.io import imread
from skimage.viewer import ImageViewer
from skimage.color import rgb2gray
from skimage import img_as_float
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

tree_roots = imread('./sample/tree-roots-resized.jpg')
crack = imread('./sample/crack-20220918204533.jpg')

# Main purpose of normalization is to make computation efficient by reducing values between 0 to 1.
def normalize_image(image):
    image_normalized = image/255
    print("color image shape:",image_normalized.shape) # row, column, color
    print("color image size:",image_normalized.size) # multiplication of HxWxC
    print("color image type:",type(image_normalized)) #numpy.ndarray
    print("color image bit depth:",image_normalized.dtype) 
    print("color image bit depth:",image_normalized.dtype)
    print(image_normalized)
    return image_normalized

def image_to_grayscale(image):
    #Y = [0.2126, 0.7152, 0.0722]
    #image_gray = img_as_float(tree_roots)@Y
    image_gray = rgb2gray(image)
    print(image_gray)
    return image_gray

def image_to_bnw(image):
    image_gray = image_to_grayscale(image)
    np.min(image_gray), np.max(image_gray)
    cutoff = np.max(image_gray)/2
    image_gray[image_gray < cutoff] = 0    # Black
    image_gray[image_gray >= cutoff] = 1 # White
    image_bnw = image_gray
    print(image_bnw)
    return image_bnw

def image_colors_comparison(image):
    image_normalized = normalize_image(image)
    image_gray = image_to_grayscale(image)
    image_bnw = image_to_bnw(image)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    ax = axes.ravel()
    ax[0].imshow(image_normalized)
    ax[0].set_title("Original")
    ax[1].imshow(image_gray, cmap=plt.cm.gray)
    ax[1].set_title("Grayscale")
    ax[2].imshow(image_bnw, cmap=plt.cm.gray)
    ax[2].set_title("Black and White")
    fig.tight_layout()
    plt.show()

image_colors_comparison(tree_roots)