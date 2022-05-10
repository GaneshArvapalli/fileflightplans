from django.db import models
import os
from django.core.exceptions import ValidationError

def validate_ppt_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pptx', '.ppt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File needs to be of PPT type. Please try again.')

def validate_kml_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.kml']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File needs to be of KML type. Please try again.')

# Create your models here.
class FlightPlan(models.Model):
    pic = models.CharField(verbose_name="Pilot in Command", max_length=150)
    vo = models.CharField(verbose_name="Visual Observer", max_length=150)
    tp = models.TextField(verbose_name="Test Personnel", blank=True)
    drone_id = models.CharField(verbose_name="FAA Number", max_length=15)
    max_speed = models.FloatField(verbose_name="Max Speed (in m/s)")
    max_altitude = models.FloatField(verbose_name="Max Altitude (in m)")
    testcardfile = models.FileField(validators=[validate_ppt_file_extension], verbose_name="Flight Test Card")
    hazardpatternfile = models.FileField(validators=[validate_ppt_file_extension], verbose_name="Hazard Pattern Card")
    kmlfile = models.FileField(validators=[validate_kml_file_extension], verbose_name="KML File")
