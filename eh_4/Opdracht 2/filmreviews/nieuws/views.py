from django.shortcuts import render
from .models import Nieuws

def nieuws(request):
    nieuwsberichten = Nieuws.objects.all().order_by('-datum')
    return render(request, 'nieuws.html', { 'nieuwsberichten':nieuwsberichten})