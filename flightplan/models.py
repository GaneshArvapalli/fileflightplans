from django.db import models
import os
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from multiselectfield import MultiSelectField
import datetime

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
    REASONS = [
       ('section_25', '107.25 - Operations from a moving vehicle or aircraft'),
       ('section_29', '107.29 - Daylight operation'),
       ('section_31', '107.31 - Visual line of sight aircraft operation'),
       ('section_33', '107.33 - Visual observer'),
       ('section_35', '107.35 - Operation of multiple sUAS'),
       ('section_37a', '107.37(a) - Yielding the right of way'),
       ('section_39', '107.39 - Operations over people'),
       ('section_41', '107.41 - Operation in certain airspace'),
       ('section_51a', '107.51(a) - Operating limitations: ground speed'),
       ('section_51c', '107.51(c) - Operating limitations: altitude'),
       ('section_51d', '107.51(d) - Operating limitations: minimum distance from clouds'),
    ]

    AIRSPACES = [
        ("class_a","Class A"),
        ("class_b","Class B"),
        ("class_c","Class C"),
        ("class_d","Class D"),
        ("class_e","Class E"),
        ("class_g","Class G"),
        ("restricted","Restricted"),
    ]

    startdate = models.DateField(verbose_name="Start Date", default=str(datetime.date.today() + datetime.timedelta(days=5)))
    enddate = models.DateField(verbose_name="End Date", default=str(datetime.date.today() + datetime.timedelta(days=65)))
    pic = models.CharField(verbose_name="Pilot in Command (PIC)", max_length=150, default="")
    vo = models.CharField(verbose_name="Visual Observers", max_length=150, blank=True)
    tp = models.TextField(verbose_name="Test Personnel", blank=True, help_text="Enter other PICs here.")
    drone_id = models.CharField(verbose_name="Drone FAA Number", max_length=15, default="")
    project_number = models.CharField(verbose_name="Internal Project Number (please don't use real ones for now)", max_length=150, default="")
    airspace = MultiSelectField(verbose_name="Classes of Airspace.", max_length=100, choices=AIRSPACES, blank=True)
    part107compliant = models.BooleanField(verbose_name="Complies with all of Part 107 and does not require Waiver or Airspace Authorization", default=True)
    restrictedairspace = models.BooleanField(verbose_name="Operations conducted in airspace controlled by entity other than the FAA (e.g. Restricted Area)", default=False)
    restrictedairspaceexplain = models.TextField(verbose_name="Explain / confirm airspace permissions. Include name, title, and phone number of person granting permissions", blank=True, help_text='If unable, write "Unable due to sponsor constraints"')
    waiver = models.BooleanField(verbose_name="Requires FAA Waiver or Airspace Authorization.", blank=True, default=False)
    waiverreason = MultiSelectField(verbose_name="Part 107 Section Waiver Reason.", max_length=100, choices=REASONS, blank=True)
    waivernumber = models.CharField(verbose_name="FAA Waiver Authorization Number", max_length=100, blank=True)
    waiverexpiration = models.DateField(verbose_name="FAA Waiver Expiration Date", default=str(datetime.date.today()))
    max_speed = models.FloatField(verbose_name="Max Speed (in m/s)", default=0)
    max_altitude = models.FloatField(verbose_name="Max Altitude AGL (in m)", default=0)
    duration = models.CharField(verbose_name="Estimated flight duration / total flight time (in hrs)", max_length=100, default="")
    testcardfile = models.FileField(validators=[validate_ppt_file_extension], verbose_name="Flight Test Card (.ppt)", blank=True)
    hazardpatternfile = models.FileField(validators=[validate_ppt_file_extension], verbose_name="Hazard Pattern Card (.ppt)", blank=True)
    kmlfile = models.FileField(validators=[validate_kml_file_extension], verbose_name="KML File (.kml)", blank=True)
    imagefile = models.ImageField(verbose_name="KML Image (.jpg, .png, .tiff or whatever)", blank=True)
    otherfile = models.FileField(verbose_name="Other files of note can be uploaded here.", blank=True)
    notes = models.TextField(verbose_name="Describe your intended flight route or the operations you will perform. Please provide an address as well.", default="")
