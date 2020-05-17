from django.shortcuts import render
from .models import PortfolioModel,PicsHappie


def homepage(request):

    project = PortfolioModel.objects.all()
    return render(request, 'portfolio/homepage.html', {'projects': project})

def picspage(request):

    picsObj = PicsHappie.objects.order_by('-picdate')
    return render(request, 'portfolio/happiepics.html', {'pics': picsObj})