from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper
import datetime

from .forms import FlightPlanForm

def index(request):
    if request.method == 'POST':
        form = FlightPlanForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                fp = form.save()
            except:
                return render(request, 'kml/properformat.html')
            strdata = fp.startdate
            outfile = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + "_flightplan_fields.txt"
            response = HttpResponse(strdata, content_type="application/text")
            response['Content-Disposition'] = "attachment; filename=%s" % outfile
            return response
    else:
        form = FlightPlanForm()
    return render(request, 'flightplan/index.html', {'form': form})
