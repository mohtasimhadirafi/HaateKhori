from django.contrib import admin

# Register your models here.
from home.models import faceDetection, image_upload


admin.site.register(faceDetection)
admin.site.register(image_upload)

