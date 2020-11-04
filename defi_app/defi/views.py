from django.shortcuts import render

from .models import Project

# Get Projects and display them
def index(request):
    return render(request, 'defi/index.html')