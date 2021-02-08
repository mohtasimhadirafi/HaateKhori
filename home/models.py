from django.core.files.base import ContentFile
from django.db import models
from .objectDetect import work
from PIL import Image
import numpy as np
from io import BytesIO
import cv2


# Create your models here.
class UploadObjectDetection(models.Model):
    image = models.ImageField(upload_to='objectDetectImages')

    def __str__(self):
        return str(self.image.url)

    def save(self, *args, **kwargs):

        #open image
        pil_img = Image.open(self.image)



        #some processing
        cv_img = np.array(pil_img)
        myImage = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        work(myImage)


        print('Image3')
        print(cv_img)

        #covert back to pil image
        im_pil = Image.fromarray(cv_img)

        #save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')

        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png),save = False)

        super().save(*args, **kwargs)


# class testObjectDetectSaveDatabase(models.Model):
#     image = models.ImageField(upload_to='objectDetectTestImages')
#     object = models.CharField()
#     x1 = models.FloatField()
#     x2 = models.FloatField()
#     x3 = models.FloatField()
#     x4 = models.FloatField()




