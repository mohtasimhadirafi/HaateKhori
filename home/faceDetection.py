import os

import cv2
import numpy as np
import face_recognition

# Global
# path = 'face_picture'
# imagePaths = os.listdir('face_picture')


def find_image_names(path, imagePaths):
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


def detect_Image(encodeListKnown, familyMemberNames, img):
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

    return img


# if __name__ == '__main__':
#     path = 'C:/Users/Ratul/PycharmProjects/HaateKhori/face_picture'
#     imagePaths = os.listdir(path)
#     familyMembersName, images = find_image_names(path,imagePaths)# pulling out names from the images
#
#
#     encodeListKnown = findEncoding(images)  # finding encodings
#
#
#     img = cv2.imread('Rafi.jpg')
#     #print(detect_Image(encodeListKnown,familyMembersName,img))
#     cv2.imshow('img', detect_Image(encodeListKnown, familyMembersName, img))# webcam
#
#     cv2.waitKey(0)
