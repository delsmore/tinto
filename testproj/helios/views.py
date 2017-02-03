from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.
def service_list(request):
    return render(request, 'helios/service_list.html', {})

def service_list(request):
    services = Service.objects.filter().order_by('servicename')
    return render(request, 'helios/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'helios/service_detail.html', {'service': service})