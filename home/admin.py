from django.contrib import admin
from .models import ObjectDetection
# Register your models here.
@admin.register(ObjectDetection)
class objectDetectionAdmin(admin.ModelAdmin):
    list_display = ('id','filename','objectName')

