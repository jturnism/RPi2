import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#RIGHT MOTOR PINS
motor1 = 23 #input
motor2 = 24 #input
motor3 = 25 #enable

#LEFT MOTOR PINS
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

def s():
	GPIO.output(all,GPIO.LOW)
	return
def f():
	GPIO.output(motor1,GPIO.HIGH)
	GPIO.output(motor2,GPIO.LOW)
	GPIO.output(motor3,GPIO.HIGH)
	GPIO.output(motor4,GPIO.HIGH)
	GPIO.output(motor5,GPIO.LOW)
	GPIO.output(motor6,GPIO.HIGH)
	return
def b():
	GPIO.output(motor1,GPIO.LOW)
	GPIO.output(motor2,GPIO.HIGH)
	GPIO.output(motor3,GPIO.HIGH)
	GPIO.output(motor4,GPIO.LOW)
	GPIO.output(motor5,GPIO.HIGH)
	GPIO.output(motor6,GPIO.HIGH)
	return
def f2():
	GPIO.output(motor1,GPIO.HIGH)
	GPIO.output(motor2,GPIO.LOW)
	GPIO.output(motor3,GPIO.HIGH)
	return
def b2():
	GPIO.output(motor1,GPIO.LOW)
	GPIO.output(motor2,GPIO.HIGH)
	GPIO.output(motor3,GPIO.HIGH)
	return
def f1():
	GPIO.output(motor4,GPIO.HIGH)
	GPIO.output(motor5,GPIO.LOW)
	GPIO.output(motor6,GPIO.HIGH)
	return
def b1():
	GPIO.output(motor4,GPIO.LOW)
	GPIO.output(motor5,GPIO.HIGH)
	GPIO.output(motor6,GPIO.HIGH)
	return
def exit():
	stop()
	GPIO.cleanup()
	print("You may now use CTRL+C")
	return

print("Commands :  s - stop")
print("			   f - forward")
print("			   b - backward")	
print("			  f1 - left motor forward")
print("			  b1 - left motor backward")	
print("			  f2 - right motor forward")
print("			  b2 - right motor backward")	
while True:
	cmd = input(">")
	func = globals()[cmd]
	func()
