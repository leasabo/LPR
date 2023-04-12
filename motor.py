import  RPi.GPIO as GPIO
from time import sleep
# GPIO.setmode(GPIO.BOARD)

# motorA_1 = 8
# motorA_2 = 10

# GPIO.setup(motorA_1, GPIO.OUT)
# GPIO.setup(motorA_2, GPIO.OUT)

def MoverMotor(x):
    #Setear los pines con numeracion de la placa
    GPIO.setmode(GPIO.BOARD)

    motorA_1 = 8 	#GPIO 14
    motorA_2 = 10	#GPIO 15
    
    #Pines provenientes del puente H
    GPIO.setup(motorA_1, GPIO.OUT)
    GPIO.setup(motorA_2, GPIO.OUT)
    
    if x == 1:				#Girar para un sentido
        GPIO.output(motorA_1, 1)
        GPIO.output(motorA_2, 0)
    elif x == 2:			#Girar para el sentido contrario
        GPIO.output(motorA_1, 0)
        GPIO.output(motorA_2, 1)
    elif x == 0:			#No girar (para el motor)
        GPIO.output(motorA_1, 0)
        GPIO.output(motorA_2, 0)

def subir():			#Procedimiento para elevar la barrera
    MoverMotor(1)
    sleep(0.135)
    MoverMotor(0)
    sleep(2)

def bajar():			#Procedimmiento para bajar la barrera
    MoverMotor(2)
    sleep(0.135)
    MoverMotor(0)
    sleep(2)
