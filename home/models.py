from django.core.files.base import ContentFile
from django.db import models
from .objectDetect import work
from PIL import Image
import numpy as np
from io import BytesIO


# Create your models here.
class UploadObjectDetection(models.Model):
    image = models.ImageField(upload_to='objectDetectImages')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        #open image
        pil_img = Image.open(self.image)



        #some processing
        cv_img = np.array(pil_img)
        img = work(cv_img)

        print('Image3')
        print(img)

        #covert back to pil image
        im_pil = Image.fromarray(img)

        #save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')

        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png),save = False)

        super().save(*args, **kwargs)





