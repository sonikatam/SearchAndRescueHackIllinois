from src import camera as camera_module
import cv2

if __name__ == '__main__':

    camera = camera_module.Camera({
        "show_preview": True
    })

    # Continuously capture frames and display them
    while True:
        camera.capture()
        image_array = camera.image_array

        # Display the image using OpenCV
        cv2.imshow("Camera Video", image_array)

        # Check for 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV window
    camera.release()
    cv2.destroyAllWindows()