from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    projects = Project.objects.all()  # grabs all object from database
    return render(request, 'portfolio/home.html', {'projects': projects})
