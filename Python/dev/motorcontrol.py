#import RPi.GPIO as GPIO
import time

PWM_min = 1000
PWM_max = 2000
PWM_step= 2500

micro = 0.000001

def Setup():
	#GPIO.setup(17, GPIO.OUT)
	pass
	
def usleep(value):
	time.sleep(value*micro)

def MotorControl(Amount):
	PWM_value = (PWM_max - PWM_min) / 100 * Amount + PWM_min
	#GPIO.output(17, True)
	usleep(PWM_value)
	#GPIO.output(17, False)
	usleep(PWM_step - PWM_value)

Setup()
MotorControl(65.5)
