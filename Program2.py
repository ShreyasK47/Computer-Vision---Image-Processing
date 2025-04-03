import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def scale_image(image, scale_x, scale_y):
    scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def translate_image(image, tx, ty):
    height, width = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    return translated_image

def main():
    image_path = 'tree.jpg'  # Replace with your image path
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return
    
    rotated = rotate_image(image, 45)
    scaled = scale_image(image, 1.5, 1.5)
    translated = translate_image(image, 50, 50)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated)
    cv2.imshow('Scaled Image', scaled)
    cv2.imshow('Translated Image', translated)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
