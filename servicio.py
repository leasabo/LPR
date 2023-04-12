from ast import If
import cv2
import motor
import sensor
import capturar
import LPR
import time
import RPi.GPIO as GPIO

#Distancia en cm a la que se acciona
margen = 75

try:
    while True:
        distancia = 100
	#Cuando la distancia detectada sea mayor al margen
        while distancia > margen:
            distancia = sensor.distance()
            print ("Distancia medida = %.1f cm" % distancia)
        
	#Tomar una foto
        capturar.clic()
	
	#Detectar los caracteres alfanumericos
        lpr = LPR.LPR()
    	
	#Simular que se ha tomado la foto 13 de la coleccion
        img = cv2.imread(f"./autos/013.png")
        txt = lpr.read_license(img)
        txt = txt.rstrip()

	#Imprimir los caracteres detectacos
        print(f"Se reconoció: {txt}")

        # Patentes habilitadas para el paso
        patentes = ["AD440CY", "AB397UK", "AD233LT", "AE182AY", "AE182AW",
                    "AE486WE", "AE796GG", "AD023DO", "AC883RA", "AC017TU",
                    "AC017TN", "AD440CY", "AA854LC", "AE497FZ", "AC017TR",
                    "AE622RT", "AD461GQ", "AA516IP", "AC724YO", "AE250FX",
                    "AE521RQ", "AC883RJ", "AE676WN", "AE410HE", "AE444JH"]

	#Si la patente es una de las habilitadas
        if txt in patentes:
            motor.subir()   #Subir la barrera
            time.sleep(5)   #esperar un breve tiempo
        
            motor.bajar()	   #y bajar la barrera

    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Parado por el usuario")
    GPIO.cleanup()
