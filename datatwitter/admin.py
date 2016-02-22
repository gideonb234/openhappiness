from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Tweet)
admin.site.register(Twitter)
admin.site.register(Dataset)
admin.site.register(Result)