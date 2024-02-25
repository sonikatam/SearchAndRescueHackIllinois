import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Check if the frame is valid
    if not ret:
        break

    cv2.imshow('Video Capture', frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()