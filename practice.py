#Exercise: Write Gamma Filter

from skimage import io
from matplotlib import pyplot as plt
g = 0.5
def gamma(x, g):
    return (x/255.)**g * 255.

img = io.imread("../Media/IMG_7093.jpg")
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
         pixel = img[y,x]
         img[y,x] = (gamma(pixel[0],g), gamma(pixel[1],g), gamma(pixel[2],g))
io.imshow(img)
plt.show()