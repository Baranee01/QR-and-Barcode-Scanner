#IMPORTING PACKAGES
import numpy as np
import cv2
import requests
import imutils
import warnings
warnings.filterwarnings('ignore')
from pyzbar.pyzbar import decode

#GETTING VIDEO FROM MOBILE
#REPLACE THE BELOW URL WITH YOUR OWN URL. MAKE SURE TO ADD "/shot.jpg" AT LAST.
url = "https://192.168.1.3:8080/shot.jpg"
video = cv2.VideoCapture(url)

#FETCHING VIDEO CONTINUOUSLY FROM THE URL
while True:
    image_response = requests.get(url,verify = False)
    image_array = np.array(bytearray(image_response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, -1)
    image = imutils.resize(image, width=720, height=1080)

    #DECODING THE IMAGE
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
