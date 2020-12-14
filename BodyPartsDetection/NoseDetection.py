import cv2

ds_factor = 0.5


def noseDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    nose_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_nose.xml')
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in nose_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Nose.JPEG', image)


def eyeDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_eye.xml')
    eye_rects = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eye_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Eye.JPEG', image)


def frontalFaceDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_frontalface_default.xml')
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Face.JPEG', image)


if __name__ == '__main__':
    noseDetection(cv2.resize(cv2.imread('Images/Input/DSCF4356.JPG'), None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA))
    eyeDetection(cv2.resize(cv2.imread('Images/Input/DSCF4356.JPG'), None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA))
    frontalFaceDetection(cv2.resize(cv2.imread('Images/Input/DSCF4356.JPG'), None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA))
