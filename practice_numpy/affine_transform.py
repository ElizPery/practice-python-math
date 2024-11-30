import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib

# Image size
height = 100
width = 100

# Create black image
image = np.zeros((height, width), dtype=np.uint8)

# Add number "1"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, '1', (width // 4, height // 2), font, 2, 255, 2, cv2.LINE_AA)

# Display and save an image
plt.imshow(image, cmap='gray')
plt.title('Згенероване зображення з цифрою "1"')
plt.show()

# Set the transformation matrix for the shift (shift by 10 pixels to the right and 50 pixels down)
M = np.float32([[1, 0, 10], [0, 1, 50]])

# Perform an affine transformation
result_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Show original and modified image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Оригінал')
plt.subplot(122), plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)), plt.title('Зсунуте')

plt.show()
