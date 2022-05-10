from django.urls import path, include

from . import views

app_name = 'kml'
urlpatterns = [
    path('', views.index, name='index'),
    path('properformat', views.properformat, name='properformat')
]

