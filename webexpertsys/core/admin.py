from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Tablet)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('tablet_property', 'property_translation', 'number')

admin.site.register(Property, PropertyAdmin)
