from django.shortcuts import render
from django.views.generic import ListView
from . import models

class AboutCatListView(ListView):
    model = models.AboutCat
