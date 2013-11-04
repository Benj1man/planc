from django.contrib import admin
from settings.models import Setting
from settings.models import Option

admin.site.register(Setting)
admin.site.register(Option)

