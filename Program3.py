import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel Filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Apply Prewitt Filter
prewitt_x = cv2.filter2D(image, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(image, -1, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
prewitt_combined = cv2.magnitude(prewitt_x.astype(np.float32), prewitt_y.astype(np.float32))

# Apply Laplacian Filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Apply Canny Edge Detector
canny_edges = cv2.Canny(image, 100, 200)

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Gabor Filter
gabor_kernel = cv2.getGaborKernel((21, 21), 5, np.pi/4, 10, 0.5, 0, ktype=cv2.CV_32F)
gabor_filtered = cv2.filter2D(image, cv2.CV_8UC3, gabor_kernel)

# Apply Median Filter
median_blur = cv2.medianBlur(image, 5)

# Display Results
filters = [image, sobel_combined, prewitt_combined, laplacian, canny_edges, 
           gaussian_blur, gabor_filtered, median_blur]
titles = ['Original', 'Sobel', 'Prewitt', 'Laplacian', 'Canny', 
          'Gaussian Blur', 'Gabor Filter', 'Median Filter']

plt.figure(figsize=(12, 8))
for i in range(len(filters)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(filters[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
