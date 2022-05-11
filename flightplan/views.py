from ast import excepthandler
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper
import datetime
import logging
from .forms import FlightPlanForm
from .handlers import handle_flight_plan

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = FlightPlanForm(request.POST, request.FILES)
        if form.is_valid():
            strdata = ""
            try:
                fp = form.save()
                strdata = handle_flight_plan(fp)
            except:
                return render(request, 'kml/properformat.html')
            outfile = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + "_flightplan_fields.txt"
            response = HttpResponse(strdata, content_type="application/text")
            response['Content-Disposition'] = "attachment; filename=%s" % outfile
            return response
    else:
        form = FlightPlanForm()
    return render(request, 'flightplan/index.html', {'form': form})
