from django.shortcuts import render
from .models import Service

# Create your views here.
def service_list(request):
    return render(request, 'helios/service_list.html', {})

def service_list(request):
    services = Service.objects.filter().order_by('servicename')
    return render(request, 'helios/service_list.html', {'services': services})