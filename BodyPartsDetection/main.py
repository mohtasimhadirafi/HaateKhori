import cv2

ds_factor = 0.5


def earDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    leftEar_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_leftear.xml')
    rightEar_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_rightear.xml')
    leftEar_rects = leftEar_cascade.detectMultiScale(gray, 1.7, 11)
    rightEar_rects = rightEar_cascade.detectMultiScale(gray, 1.7, 11)
    for (x, y, w, h) in leftEar_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    for (x, y, w, h) in rightEar_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Ears.JPEG', image)


def mouthDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mouth_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_mouth.xml')
    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    for (x, y, w, h) in mouth_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Mouth.JPEG', image)
    cv2.imshow("Mouth", image)
    cv2.waitKey(0)


def noseDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    nose_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_nose.xml')
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in nose_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Nose.JPEG', image)
    cv2.imshow("Nose", image)
    cv2.waitKey(0)


def eyeDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_eye.xml')
    eye_rects = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eye_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Eye.JPEG', image)
    cv2.imshow("Eye", image)
    cv2.waitKey(0)


def frontalFaceDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_frontalface_default.xml')
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('Images/Output/Face.JPEG', image)
    cv2.imshow("Face", image)
    cv2.waitKey(0)


def runDetectionMethods(image):
    noseDetection(cv2.resize(cv2.imread('Images/Input/' + image), None, fx=ds_factor, fy=ds_factor,
                             interpolation=cv2.INTER_AREA))
    eyeDetection(cv2.resize(cv2.imread('Images/Input/' + image), None, fx=ds_factor, fy=ds_factor,
                            interpolation=cv2.INTER_AREA))
    frontalFaceDetection(cv2.resize(cv2.imread('Images/Input/' + image), None, fx=ds_factor, fy=ds_factor,
                                    interpolation=cv2.INTER_AREA))
    mouthDetection(cv2.resize(cv2.imread('Images/Input/' + image), None, fx=ds_factor, fy=ds_factor,
                              interpolation=cv2.INTER_AREA))
    earDetection(cv2.resize(cv2.imread('Images/Input/' + image), None, fx=ds_factor, fy=ds_factor,
                            interpolation=cv2.INTER_AREA))


if __name__ == '__main__':
    runDetectionMethods("3.jpg")
    cv2.destroyAllWindows()
