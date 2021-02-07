import os

from django.db import models
from numpy import asarray

from .faceDetection import find_image_names, findEncoding, detect_Image
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# Create your models here.

class faceDetection(models.Model):
    image = models.ImageField(upload_to='faceDetection_result_dump')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # open image
        pil_img = asarray(Image.open(self.image))
        #print(type(pil_img))

        path = 'C:/Users/Ratul/PycharmProjects/HaateKhori/face_picture'
        imagePaths = os.listdir(path)

        familyMembersName, images = find_image_names(path, imagePaths)  # pulling out names from the images

        encodeListKnown = findEncoding(images)  # finding encodings

        img = detect_Image(encodeListKnown, familyMembersName, pil_img)

        #print(type(img))
        # convert back to pil image
        im_pil = Image.fromarray(img, mode='RGB')

        # print(type(im_pil))

        im_pil.save("faceDetection_result_dump/result.jpg")
