# from src import camera as camera_module
# import cv2

# if __name__ == '__main__':

#     camera = camera_module.Camera({
#         "show_preview": True
#     })

#     # Continuously capture frames and display them
#     while True:
#         camera.capture()
#         image_array = camera.image_array

#         # Display the image using OpenCV
#         cv2.imshow("Camera Video", image_array)

#         # Check for 'q' key to exit the loop
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera and close OpenCV window
#     camera.release()
#     cv2.destroyAllWindows()

import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

# Initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warmup
time.sleep(0.1)

# Capture video frames
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Display the image
    cv2.imshow("Video", image)
    
    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # Check for the 'q' key to exit the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()
camera.close()
