from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CloudServiceProvider)
admin.site.register(Service)
admin.site.register(VPS)
admin.site.register(DetectSetting)