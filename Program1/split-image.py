import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpeg')

# Get the height and width of the image
height, width, _ = image.shape

# Find the center of the image
center_x, center_y = width // 2, height // 2

# Copy the original image to draw lines on it
image_with_lines = image.copy()

# Draw black lines to divide the image into quadrants
# Vertical line (from top to bottom)
cv2.line(image_with_lines, (center_x, 0), (center_x, height), (0, 0, 0), 2)

# Horizontal line (from left to right)
cv2.line(image_with_lines, (0, center_y), (width, center_y), (0, 0, 0), 2)

# Partition the image into four quadrants
quadrant_1 = image[0:center_y, 0:center_x]  # Top-left
quadrant_2 = image[0:center_y, center_x:]   # Top-right
quadrant_3 = image[center_y:, 0:center_x]   # Bottom-left
quadrant_4 = image[center_y:, center_x:]    # Bottom-right

# Display the quadrants and the image with lines drawn
cv2.imshow('Image with Quadrants', image_with_lines)
cv2.imshow('Quadrant 1 (Top-Left)', quadrant_1)
cv2.imshow('Quadrant 2 (Top-Right)', quadrant_2)
cv2.imshow('Quadrant 3 (Bottom-Left)', quadrant_3)
cv2.imshow('Quadrant 4 (Bottom-Right)', quadrant_4)

# Wait until a key is pressed and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
