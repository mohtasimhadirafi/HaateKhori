import os

import cv2
import numpy as np
import face_recognition

# Global
path = 'face_picture'
imagePaths = os.listdir(path)


def find_image_names():
    familyMemberNames = []
    images = []
    for cls in imagePaths:
        currentImage = cv2.imread(f'{path}/{cls}')
        images.append(currentImage)
        familyMemberNames.append(os.path.splitext(cls)[0])

    return familyMemberNames, images


def findEncoding(images):
    encode_list = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


def webcam_capture(encodeListKnown, familyMemberNames):
    capture = cv2.VideoCapture(0)
    while True:
        success, img = capture.read()
        imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
        faceLocations = face_recognition.face_locations(imgSmall)
        encodes = face_recognition.face_encodings(imgSmall, faceLocations)

        for encodeFace, faceLoc in zip(encodes, faceLocations):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.50 and matches[matchIndex]:
                name = familyMemberNames[matchIndex].upper()
                # print(name)
            else:
                name = 'Unknown'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('webcam', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    familyMembersName, images = find_image_names()  # pulling out names from the images
    encodeListKnown = findEncoding(images)  # finding encodings
    webcam_capture(encodeListKnown, familyMembersName)  # webcam
