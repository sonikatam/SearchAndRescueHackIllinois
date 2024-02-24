import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Preprocess the image (if needed)
    # Perform image recognition processing (use an existing model or algorithm)

    # Display the processed image
    cv2.imshow('Processed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# turn LED light on when recognized 


import cv2
from gpiozero import LED

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize GPIO pin (change the pin number as needed)
led = LED(17)  # Example: GPIO pin 17

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Turn on the GPIO pin when a face is detected
        led.on()
    else:
        # Turn off the GPIO pin when no face is detected
        led.off()

    # Display the frame
    cv2.imshow('Image Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
