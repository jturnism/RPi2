import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#motor 1 pins RIGHT MOTOR
motor1 = 23 # Input Pin
motor2 = 24 # Input Pin
motor3 = 25 # Enable Pin

#motor 2 pins LEFT MOTOR
motor4 = 17 #input
motor5 = 27 #input
motor6 = 22 #enable

all = motor1,motor2,motor3,motor4,motor5,motor6

GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)
GPIO.setup(motor3,GPIO.OUT)
GPIO.setup(motor4,GPIO.OUT)
GPIO.setup(motor5,GPIO.OUT)
GPIO.setup(motor6,GPIO.OUT)

print("FORWARD MOTION RIGHT MOTOR")
GPIO.output(motor1,GPIO.HIGH)
GPIO.output(motor2,GPIO.LOW)
GPIO.output(motor3,GPIO.HIGH)

print("FORWARD MOTION LEFT MOTOR")
GPIO.output(motor4,GPIO.HIGH)
GPIO.output(motor5,GPIO.LOW)
GPIO.output(motor6,GPIO.HIGH)

sleep(10)

print("BACKWARD MOTION RIGHT MOTOR")
GPIO.output(motor1,GPIO.LOW)
GPIO.output(motor2,GPIO.HIGH)
GPIO.output(motor3,GPIO.HIGH)

print("BACKWARd MOTION LEFT MOTOR")
GPIO.output(motor4,GPIO.LOW)
GPIO.output(motor5,GPIO.HIGH)
GPIO.output(motor6,GPIO.HIGH)

sleep(10)

print("STOP")
GPIO.output(all,GPIO.LOW)

GPIO.cleanup()
