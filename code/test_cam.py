from src import camera as camera_module
import time
import cv2
import numpy as np
import threading

# Function to send images over a network
def send_image(image_array, host, port):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    _, img_encoded = cv2.imencode('.jpg', image_array, encode_param)
    
    # Create a socket connection and send the encoded image
    # You may need to replace this with your specific networking code
    # For example, you can use sockets, MQTT, etc.
    # Here, we're just printing the size of the encoded image for demonstration purposes.
    print(f"Sending image of size: {len(img_encoded)} bytes")

# Function to continuously capture and send images
def capture_and_send(camera, host, port, total_seconds, sample_hz):
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        image_array = camera.capture()
        send_image(image_array, host, port)

        time.sleep(max(0, 1/sample_hz - (time.time() - start_time)))

if __name__ == '__main__':
    total_seconds = 60
    sample_hz = 10

    # Replace "your_laptop_ip" with the IP address of your laptop
    host = "10.194.242.78"
    port = 12345  # Choose a suitable port

    camera = camera_module.Camera({
        "show_preview": False
    })

    # Start a thread for capturing and sending images
    capture_thread = threading.Thread(target=capture_and_send, args=(camera, host, port, total_seconds, sample_hz))
    capture_thread.start()

    # Receive images on your laptop using OpenCV
    # You need to run this code on your laptop, not on the Raspberry Pi
    server_socket = cv2.VideoCapture(f"tcp://{host}:{port}")
    while True:
        ret, frame = server_socket.read()
        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    server_socket.release()
    cv2.destroyAllWindows()
