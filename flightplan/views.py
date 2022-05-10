from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper

from .forms import FlightPlanForm

def index(request):
    if request.method == 'POST':
        form = FlightPlanForm(request.POST, request.FILES)
        # if form.is_valid():
            # try:
            #     strdata = handle_uploaded_file(request.FILES['file'], form.cleaned_data)
            # except:
            #     return properformat(request)
            # outfile = request.FILES['file'].name[:-4] + "_auto.kml"
            # response = HttpResponse(strdata, content_type="application/kml")
            # response['Content-Disposition'] = "attachment; filename=%s" % outfile
            # return response
            # return render(request, 'flightplan/index.html', {'form': form})
    else:
        form = FlightPlanForm()
    return render(request, 'flightplan/index.html', {'form': form})
