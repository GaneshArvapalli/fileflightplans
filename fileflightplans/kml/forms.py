from django import forms
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.kml']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File needs to be of KML type. Please try again.')

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_extension])
    max_speed = forms.FloatField()
