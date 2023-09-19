from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import portfolio


# Create your views here.
def index(request):
    mod = portfolio.objects.all()
    param = {"mod" : mod}
    return render(request, 'index.html', param)
 