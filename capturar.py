import cv2
import uuid

puerto_cam = 0  # Hardcodeado para la cámara 0

def clic():
	cap = cv2.VideoCapture(puerto_cam)
	leido, frame = cap.read()

	if leido == True:
		nombre_foto = str(uuid.uuid4()) + ".png" # uuid4 regresa un objeto, no una cadena. Por eso se lo convierte
		cv2.imwrite(nombre_foto, frame)
		#Imprimir el nombre de la foto tomada
		print("Foto tomada existosamente: {}".format(nombre_foto))
	else:
		print("Error al acceder a la cámara")
    	# Por último, se libera la cámara
	cap.release()
