import time
import threading
#import RPi.GPIO as GPIO

#### Settings ####
####   Pins   ####
Motor1		= 17
Motor2		= 18
Motor3		= 19
Motor4		= 20
LEDS		= 21
THRO		= 22
PTCH		= 23
ROLL		= 24
AILE		= 25

####   Time   ####
micro		= 0.000001

####   PWM    ####
PWM_min		= 1000
PWM_max 	= 2000
PWM_step	= 2500

####   Gyro   ####
GyroI2C		= 0x69
GyroYaw		= 0
GyroPitch	= 0
GyroRoll	= 0

#### Offsets  ####
M1Offset	= 0
M2Offset	= 0
M3Offset	= 0
M4Offset	= 0

#### Motorval ####
M1PWM		= 1000
M2PWM		= 1000
M3PWM		= 1000
M4PWM		= 1000

# Basic Functions
def usleep(value):
	time.sleep(value * micro)

# Setup
def setup():
	RaspiSetup()
	I2CSetup()

def RaspiSetup():
	GPIO.setup(Motor1, GPIO.OUT)
	GPIO.setup(Motor2, GPIO.OUT)
	GPIO.setup(Motor3, GPIO.OUT)
	GPIO.setup(Motor4, GPIO.OUT)

def I2CSetup():
	pass

def MotorThreadsStart():
	MotorThread1 = MotorControlM1()
	MotorThread2 = MotorControlM2()
	MotorThread3 = MotorControlM3()
	MotorThread4 = MotorControlM4()
	MotorThread1.start()
	MotorThread2.start()
	MotorThread3.start()
	MotorThread4.start()
	#MotorThread1.join()
	#MotorThread2.join()
	#MotorThread3.join()
	#MotorThread4.join()

# Reading Functions


# Writing Funtions
def MotorControlM1():
	GPIO.output(Motor1, True)
	usleep(M2PWM)
	GPIO.output(Motor1, False)
	usleep(PWM_step-M2PWM)

def MotorControlM2():
	GPIO.output(Motor2, True)
	usleep(M2PWM)
	GPIO.output(Motor2, False)
	usleep(PWM_step-M2PWM)

def MotorControlM3():
	GPIO.output(Motor3, True)
	usleep(M3PWM)
	GPIO.output(Motor3, False)
	usleep(PWM_step-M3PWM)

def MotorControlM4():
	GPIO.output(Motor4, True)
	usleep(M4PWM)
	GPIO.output(Motor4, False)
	usleep(PWM_step-M4PWM)

# Main
def main():
	setup()
	MotorThreads()

main()