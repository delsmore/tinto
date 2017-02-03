from django.contrib import admin
from .models import Service
from .models import Institution
from .models import Licence


admin.site.register(Service)
admin.site.register(Institution)
admin.site.register(Licence)