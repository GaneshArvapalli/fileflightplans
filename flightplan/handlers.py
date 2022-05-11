# Ganesh Arvapalli
## 5-11-2022
from django.core import serializers
import logging
import json
from .models import FlightPlan

logger = logging.getLogger(__name__)

def handle_flight_plan(data):
    strdata = serializers.serialize(
        "json", 
        [data, ],
        fields=[
            "pic", 
            "vo", 
            "tp", 
            "drone_id", 
            "project_number", 
            "part107compliant", 
            "airspace", 
            "restrictedairspace", 
            "restrictedairspaceexplain", 
            'waiver', 
            'waiverreason', 
            "waivernumber", 
            "waiverexpiration", 
            "max_speed", 
            "max_altitude", 
            "duration", 
            "notes", 
            "startdate", 
            "enddate"
        ]
    )
    # Prettier formatting
    obj = json.loads(strdata)
    strdata = json.dumps(obj, indent=4)
    return strdata

# Currently missing: "testcardfile", "hazardpatternfile", "kmlfile", "imagefile", "otherfile", 