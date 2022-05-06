from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper

from .forms import UploadFileForm
from .handlers import handle_uploaded_file

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            strdata = handle_uploaded_file(request.FILES['file'], form.cleaned_data)
            outfile = request.FILES['file'].name[:-4] + "_auto.kml"
            response = HttpResponse(strdata, content_type="application/kml")
            response['Content-Disposition'] = "attachment; filename=%s" % outfile
            return response
    else:
        form = UploadFileForm()
    return render(request, 'kml/index.html', {'form': form})

def success(request):
    return render(request, 'kml/success.html')
