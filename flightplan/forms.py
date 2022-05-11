from django import forms
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import FlightPlan

def validate_ppt_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pptx', '.ppt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File needs to be of PPT type. Please try again.')

def validate_ppt_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.kml']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File needs to be of KML type. Please try again.')

class FlightPlanForm(forms.ModelForm):
    class Meta:
        model = FlightPlan
        fields = ["pic", "vo", "tp", "drone_id", "project_number", "part107compliant", "airspace", "restrictedairspace", "restrictedairspaceexplain",
                    'waiver', 'waiverreason', "waivernumber", "waiverexpiration", "max_speed", "max_altitude", "duration", "testcardfile", "hazardpatternfile", "kmlfile", 
                    "imagefile", "otherfile", "notes", "startdate", "enddate"]
        widgets = {
            'tp': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'restrictedairspaceexplain': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
            'notes': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
            'otherfile': forms.FileInput(attrs={'multiple': True, 'required': False})
        }