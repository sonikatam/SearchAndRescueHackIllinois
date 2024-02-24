import cv2
import picamera
import picamera.array

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

# Initialize the PiCamera
with picamera.PiCamera() as camera:
    # Set camera resolution (adjust as needed)
    camera.resolution = (640, 480)

    # Create a stream for capturing images
    with picamera.array.PiRGBArray(camera) as stream:
        # Continuously capture frames from the camera
        for frame in camera.capture_continuous(stream, format="bgr", use_video_port=True):
            # Convert the frame to a numpy array
            image = frame.array

            # Display the frame in the OpenCV window
            cv2.imshow("Camera Feed", image)

            # Wait for a key press and check if the 'q' key was pressed
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            # Clear the stream in preparation for the next frame
            stream.truncate(0)

# Clean up
cv2.destroyAllWindows()
