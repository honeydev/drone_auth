from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    """Render base template."""
    return render(request, 'index.html')
