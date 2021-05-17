#IMPORTING PACKAGES
import numpy as np
import cv2
from pyzbar.pyzbar import decode

#OPENING WEBCAM
webcam = cv2.VideoCapture(0)

while True:
    #READING IMAGE FROM WEBCAM
    value, image = webcam.read()

    #DECODING THE TEXT PRESENT IN THE QR CODE
    for qrcode in decode(image):
        mydata = qrcode.data.decode("UTF-8")
        print(mydata)

        #DETECTING QR CODE USING OUTLINE
        points = np.array([qrcode.polygon], np.int64)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(image, [points], True, (0, 255, 0), 5)

    #DISPLAYING WINDOW
    cv2.imshow("QR Code Scanner", image)
    if cv2.waitKey(1) == ord("q"):
        break

#CLOSING ALL WINDOWS
cv2.destroyAllWindows()
