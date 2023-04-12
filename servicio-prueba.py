from ast import If
import cv2
import motor
import sensor
import capturar
import LPR
import time
import RPi.GPIO as GPIO

margen = 75

try:
    while True:
#        distancia = 100
#        while distancia > margen:
#            distancia = sensor.distance()
#            print ("Distancia medida = %.1f cm" % distancia)
        
        capturar.clic()

        lpr = LPR.LPR()
    
        img = cv2.imread(f"./autos/013.png")
        txt = lpr.read_license(img)
        txt = txt.rstrip()
        print(f"Se reconoció: {txt}")

        # Patentes habilitadas para el paso
        patentes = ["AD440CY", "AB397UK", "AD233LT", "AE182AY", "AE182AW",
                    "AE486WE", "AE796GG", "AD023DO", "AC883RA", "AC017TU",
                    "AC017TN", "AD440CY", "AA854LC", "AE497FZ", "AC017TR",
                    "AE622RT", "AD461GQ", "AA516IP", "AC724YO", "AE250FX",
                    "AE521RQ", "AC883RJ", "AE676WN", "AE410HE", "AE444JH"]

        if txt in patentes:
            motor.subir()
            time.sleep(5)
        
        motor.bajar()

    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Parado por el usuario")
    GPIO.cleanup()
