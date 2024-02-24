import RPi.GPIO as GPIO
import time
from src import motor as motor_module
import numpy as np
from src import distance_sensor as distance_sensor_module
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


if __name__ == '__main__':

    motor1 = motor_module.Motor({
        "pins": {
            "speed": 13,
            "control1": 5,
            "control2": 6
        }
    })

    motor2 = motor_module.Motor({
        "pins": {
            "speed": 12,
            "control1": 7,
            "control2": 8
        }
    })
    
    distance_sensor1 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 23,
            "trigger": 24
        }
    })
    
    total_seconds = 60
    sample_hz = 2
    
    TRIG = 17
    ECHO = 27
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)


    speeds = list(np.linspace(0, 1, 11)) + list(np.linspace(0.9, 0, 10))

    dt = 0.25
    motor1.stop()
    motor2.stop()
    time.sleep(dt)
    
    def move_forward():
        motor1.forward(1)  # Move forward at full speed
        motor2.forward(1)  # Move forward at full speed
    
    def move_backward():
        motor1.backward(1)  # Move forward at full speed
        motor2.backward(1)

    def stop_motors():
        motor1.stop()
        motor2.stop()
    
    try:
        while True:
            print("in while loop")
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            start_time = time.time()
            loop_start = time.time()
            print("Sensor 1: ", distance_sensor1.distance)

            print("checking distance")
            if distance_sensor1.distance < 0.3:  # Adjust distance threshold as needed
                print("Obstacle detected! Moving backward...")
                move_forward()  # Move backward when obstacle detected
                time.sleep(1) 
            else:
                print("move forward")
                move_backward()
                time.sleep(0.1)
            # move_forward()  # Move forward continuously
            # time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program stopped by user")
        stop_motors()
        GPIO.cleanup()
    
    print("stopping")
    motor1.stop()
    motor2.stop()


