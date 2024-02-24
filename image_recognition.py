import cv2
import numpy as np

def image_recognition(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image (if needed)
    # Perform image recognition processing (use an existing model or algorithm)

    # Display the processed image
    cv2.imshow('Processed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Specify the path to the image captured by the OV5647 camera
    image_path = 'path_to_your_image.jpg'
    
    # Call the image recognition function
    image_recognition(image_path)
