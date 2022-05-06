from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

# from .models import Book, Thoughts

def index(request):
    return HttpResponse("Hello Django website!")