from django.core.files.base import ContentFile
from django.db import models
from .objectDetect import work
from PIL import Image
import numpy as np
from io import BytesIO
import cv2
from _collections import defaultdict
import random

functionDict = defaultdict(list)

# Create your models here.
class ObjectDetection(models.Model):

    image = models.ImageField(upload_to='images/', null=True)

    filename = models.TextField(max_length=500)
    objectName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        #open image
        pil_img = Image.open(self.image)



        #some processing
        cv_img = np.array(pil_img)
        myImage = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)


        functionDict = work(myImage)


        for i in functionDict.keys():
            print('dictionary')
            print(i)
            print('before initialization')

            # print('after initialization')
            # obj.image = self.image
            obj = ObjectDetection()
            print('after image')
            print(i)
            self.id = random.getrandbits(32)
            self.filename = i
            print(functionDict[i])
            self.objectName = functionDict[i]
            super().save()




        # #covert back to pil image
        # im_pil = Image.fromarray(cv_img)
        #
        # #save
        # buffer = BytesIO()
        # im_pil.save(buffer, format='png')
        #
        # image_png = buffer.getvalue()

        #self.image.save(str(self.image), ContentFile(image_png),save = False)

        super().save(*args, **kwargs)







