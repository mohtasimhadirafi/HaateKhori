import cv2

ds_factor = 0.5


def getCascade(action):
    switcher = {
        'mouth': cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_mouth.xml'),
        'nose': cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_nose.xml'),
        'eye': cv2.CascadeClassifier('CascadeFiles/haarcascade_eye.xml'),
        'frontalFace': cv2.CascadeClassifier('CascadeFiles/haarcascade_frontalface_default.xml'),
    }
    return switcher.get(action, "nothing")


def bodyPartDetection(image, action):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = getCascade(action)
    rects = cascade.detectMultiScale(gray, 1.7, 11)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    location = 'Images/Output/' + action + '.JPEG'
    cv2.imwrite(location, image)
    cv2.imshow(action, image)
    cv2.waitKey(0)


if __name__ == '__main__':
    bodyPartDetection(cv2.resize(cv2.imread('Images/Input/' + "1.jpg"), None, fx=ds_factor, fy=ds_factor,
                                 interpolation=cv2.INTER_AREA), "nose")
    cv2.destroyAllWindows()