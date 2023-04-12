import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#Seteo de los pines
GPIO_TRIGGER	= 16	#GPIO 23
GPIO_ECHO 	= 18	#GPIO 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    #Tiempo transcurrido como diferencia entre inicio y parada
    TimeElapsed = StopTime - StartTime
    # Multiplicado por la velocidad del sonido (34300 cm/s)
    # y dividido por 2, considerando la ida y vuelta de la senial
    distance = (TimeElapsed * 34300) / 2

    return distance

def medir():
    try:
        while True:
            dist = distance()
	    # Imprimir la distancia en centimetros
            print ("Distancia medida = %.1f cm" % dist)
            time.sleep(1)
 
        # Resetear presionando CTRL + C
    except KeyboardInterrupt:
        print("Parado por el usuario")
        GPIO.cleanup()

 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Distancia medida = %.1f cm" % dist)
            time.sleep(1)
 
        # Resetear presionando CTRL + C
    except KeyboardInterrupt:
        print("Parado por el usuario")
        GPIO.cleanup()
