from django.shortcuts import render, get_object_or_404
from .models import Service
from .models import Institution
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from helios.serializers import ServiceSerializer

# Create your views here.


def service_list(request):
    services = Service.objects.filter(activeflag=1).order_by('servicename')
    return render(request, 'helios/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'helios/service_detail.html', {'service': service})

def institution_list(request):
    institutions = Institution.objects.filter().order_by('instname')
    return render(request, 'helios/institution_list.html', {'institutions': institutions})

def institution_detail(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    return render(request, 'helios/institution_detail.html', {'institution': institution})




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def api_service_list(request):
    """
    List all services

    """
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return JSONResponse(serializer.data)

def api_service_detail(request, pk):
    """
    Retrieve a service.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return JSONResponse(serializer.data)


