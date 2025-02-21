import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np

img = im.imread("image.png")
print(img.shape)

imgData = np.array(img)

plt.imshow(imgData)
plt.show()

rotatedImg = np.rot90(imgData)
plt.imshow(rotatedImg)
plt.show()

flippedImg = np.fliplr(imgData)
plt.imshow(flippedImg)
plt.show()

grayImg = np.dot(img, [0.299, 0.587, 0.114])
plt.imshow(grayImg, cmap='gray')
plt.show()