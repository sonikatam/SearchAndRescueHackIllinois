import RPi.GPIO as GPIO
import time
from src import motor as motor_module
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define motor pins
motor_pins = {
    "speed": 13,
    "control1": 5,
    "control2": 6
}

# Initialize motors
motor1 = motor_module.Motor({"pins": motor_pins})
motor2 = motor_module.Motor({"pins": motor_pins})  # Assuming same motor configuration

# Define motor speeds
speeds = list(np.linspace(0, 1, 11)) + list(np.linspace(0.9, 0, 10))

# Define delay time
dt = 0.25

# Define ultrasonic sensor pins
TRIG = 17
ECHO = 27

# Set up ultrasonic sensor
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def stop_motors():
    motor1.stop()
    motor2.stop()

def move_forward(speed):
    motor1.forward(speed)
    motor2.forward(speed)

def move_backward(speed):
    motor1.backward(speed)
    motor2.backward(speed)

def turn_right():
    motor1.forward(0.5)  # Adjust speed for turning
    motor2.backwar
