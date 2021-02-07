import cv2


def getCascade(action):
    switcher = {
        'mouth': cv2.CascadeClassifier('home/CascadeFiles/haarcascade_mcs_mouth.xml'),
        'nose': cv2.CascadeClassifier('home/CascadeFiles/haarcascade_mcs_nose.xml'),
        'eye': cv2.CascadeClassifier('home/CascadeFiles/haarcascade_eye.xml'),
        'frontalFace': cv2.CascadeClassifier('home/CascadeFiles/haarcascade_frontalface_default.xml'),
    }
    return switcher.get(action, "nothing")


def bodyPartDetection(image, action):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = getCascade(action)
    rects = cascade.detectMultiScale(gray, 1.7, 11)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return image