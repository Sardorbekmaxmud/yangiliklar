from django.contrib import admin
from django.apps import apps
from . import models

# Register your models here.
for model in apps.get_app_config('yangiliklar').models.values():
    admin.site.register(model)