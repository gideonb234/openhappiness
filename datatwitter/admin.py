from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Tweets)
admin.site.register(Dataset)
admin.site.register(DatasetResult)
admin.site.register(QueryResult)