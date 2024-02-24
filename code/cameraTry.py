import time
import matplotlib.pyplot as plt
from src import camera as camera_module

if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 10

    camera = camera_module.Camera({
        "show_preview": False
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        image_array = camera.image_array

        # Display the image
        plt.imshow(image_array)
        plt.show()

        time.sleep(max(0, 1/sample_hz - (time.time() - start_time)))