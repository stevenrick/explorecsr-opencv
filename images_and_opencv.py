import cv2  # conda install -c conda-forge opencv
import numpy as np
from matplotlib import pyplot as plt  # conda install matplotlib
from PIL import Image  # conda install pillow

img_color = Image.open('cat.jpg')
img_grey = img_color.convert('L')

# plt.subplot(121), plt.imshow(img_color)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img_grey, cmap='gray')
# plt.title('Greyscale Image'), plt.xticks([]), plt.yticks([])

img_color_array = np.asarray(img_color)
img_grey_array = np.asarray(img_grey)

# edges1 = cv2.Canny(img_grey_array, 5, 10)
# edges2 = cv2.Canny(img_grey_array, 10, 25)
# edges3 = cv2.Canny(img_grey_array, 25, 50)
#
# plt.subplot(141), plt.imshow(img_color)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(142), plt.imshow(edges1, cmap='gray')
# plt.title('Edge Image 1'), plt.xticks([]), plt.yticks([])
# plt.subplot(143), plt.imshow(edges2, cmap='gray')
# plt.title('Edge Image 2'), plt.xticks([]), plt.yticks([])
# plt.subplot(144), plt.imshow(edges3, cmap='gray')
# plt.title('Edge Image 3'), plt.xticks([]), plt.yticks([])

# img_filtered = cv2.bilateralFilter(img_color_array, 100, 200, 200)
# plt.subplot(121), plt.imshow(img_color)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img_filtered)
# plt.title('Image after Filter'), plt.xticks([]), plt.yticks([])

# img_gray_filtered = cv2.bilateralFilter(img_grey_array, 25, 50, 50)
# plt.subplot(121), plt.imshow(img_grey, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img_gray_filtered, cmap='gray')
# plt.title('Image after Filter'), plt.xticks([]), plt.yticks([])

# img_gray_filtered = cv2.bilateralFilter(img_grey_array, 25, 50, 50)
# edges_filtered = cv2.Canny(img_gray_filtered, 10, 25)
# plt.subplot(121), plt.imshow(img_color)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges_filtered, cmap='gray')
# plt.title('Edge Image after Filter'), plt.xticks([]), plt.yticks([])

img_grey_edge = cv2.Canny(img_grey_array, 25, 50)
img_gray_filtered = cv2.bilateralFilter(img_grey_array, 25, 50, 50)
edges_filtered = cv2.Canny(img_gray_filtered, 10, 25)
plt.subplot(131), plt.imshow(img_color)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_grey_edge, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(edges_filtered, cmap='gray')
plt.title('Edge Image after Filter'), plt.xticks([]), plt.yticks([])

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
