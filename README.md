# QR and Barcode Scanner

Implementation of real time QR and Barcode scanner using Python and OpenCV.

##
### FILES ATTACHED
- qrscanner.py (Scanning is done using webcam)
- qrscannermobile.py (Scanning is done using mobile camera)

##
### INSTALLATION

###
This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [OpenCV](https://opencv.org/)
- [Pyzbar](https://pypi.org/project/pyzbar/)
- [Requests](https://pypi.org/project/requests/)
- [Imutils](https://pypi.org/project/imutils/)

###
Use this command to install OpenCV
```bash
pip install opencv-python
```

Use this command to install Pyzbar
```bash
pip install pyzbar
```

Use this command to install Imutils
```bash
pip install imutils
```
##
### CONNECTING MOBILE CAMERA TO PC

- Download and install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) application on your mobile phone.
- Make sure to connect both your PC and Mobile to the same network. Open "**IP Webcam**" application on your mobile and click "**Start Server**" (usually found at the bottom). This will open the camera of your mobile.
- A URL is being displayed on the mobile screen, type the same URL on your PC browser, and under "**Video renderer**" Section, click on "**Javascript**".
- Video Footage from your mobile will be displayed on the browser.

##
### EXECUTION

In terminal or command window, navigate to the project directory `QR-and-Barcode-Scanner/` and run the following command:
```bash
python -m qrscanner.py
```
or

```bash
python -m qrscannermobile.py
```

##
### SCREENSHOTS

#### 1) IMAGE FROM WEBCAM :
![QR Screenshot1](https://user-images.githubusercontent.com/80042740/118488356-46932780-b739-11eb-9c6f-bf7c11274bd0.png)

###
#### 2) IMAGE FROM MOBILE CAMERA :
![QR Screenshot2](https://user-images.githubusercontent.com/80042740/118522923-3a6b9200-b75a-11eb-8dac-8692df47375d.png)
